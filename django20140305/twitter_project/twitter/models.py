from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    text = models.TextField(max_length=140)
    published_on = models.DateTimeField()
    user = models.ForeignKey(User)