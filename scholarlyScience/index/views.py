from django.shortcuts import render
from .models import *


def apphome(request):
    list1=[]
    list2=[]
    list3=[]
    
    content=companies.objects.all()
    skills=skill.objects.all()

    for i in skills:
        list3.append(i.skills)    
    
    for i in content:
        list1.append(i.location)
        list2.append(i.assignment)

    list_set=set(list1)
    list_assignment=set(list2)
    list_tech=set(list3)
    
    assignment=request.GET.get( 'assignment')
    location=request.GET.get('location')
    tech=request.GET.get('tech')
    
    content_list=[]
    if assignment != None:
        content=companies.objects.filter( assignment=assignment)
    
    elif location !=None:
        content=companies.objects.filter( location=location)
        # print(content, "111111111111111")
    elif tech !=None:
        for i in content:
            if(i.cskill.filter(skills=tech)):
                content_list.append(i)
        content=content_list
        # print(content, "111111111111111")
    else:
        ''
    
    return render(request, 'index/home.html', {'content':content, 'list_set':list_set,'list_assignment':list_assignment, 'list_tech':list_tech })
