import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scholarlyScience.settings')

import django
django.setup()

from index.models import *
from faker import Faker

obj=Faker()

def call(N):
    num=1
    for i in range(N):
        # mid=obj.bothify(text='?#??####?', letters='ABCDEWXY')
        job=obj.job()
        # timezone=obj.timezone()
        # instance=companies.objects.get(id=1)
        skill_obj=skill.objects.get_or_create(skill=job,)[0]

        
        num+=1

if __name__== '__main__':

    print("Filling Random data\n")
    call(50)
    print("Filling done")
