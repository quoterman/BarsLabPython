from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=10)
    group_date = models.DateTimeField()
    def __unicode__(self):
        return self.group_name

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group)
    def __unicode__(self):
        return self.student_name
