from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=10)
    group_date = models.DateField()
    def __unicode__(self):
        return self.group_name

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_group = models.ForeignKey(Group)
    def __unicode__(self):
        return self.student_name