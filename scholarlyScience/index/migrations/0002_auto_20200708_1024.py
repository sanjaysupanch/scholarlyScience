# Generated by Django 3.0.7 on 2020-07-08 10:24

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Logo', models.URLField()),
                ('NoofAssignments', models.IntegerField()),
                ('if_updated', models.BooleanField(default=True)),
                ('NoofOpenings', models.IntegerField()),
                ('tags', django_mysql.models.ListTextField(models.CharField(max_length=100), default='', size=None)),
                ('Description', models.TextField(default='')),
                ('tech_stack', django_mysql.models.ListTextField(models.CharField(max_length=100), default='', size=None)),
                ('openings_tags', django_mysql.models.ListTextField(models.CharField(max_length=100), default='', size=None)),
                ('location', django_mysql.models.ListTextField(models.CharField(max_length=100), default='', size=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='companie',
        ),
        migrations.DeleteModel(
            name='companies',
        ),
        migrations.DeleteModel(
            name='skill',
        ),
    ]