__author__ = 'Artur'
from django.contrib import admin
from groups.models import Group, Student

admin.site.register(Group)
admin.site.register(Student)