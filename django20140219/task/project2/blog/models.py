from django.db import models

class Post(models.Model):
    post_text = models.CharField(max_length = 1000)
    post_title = models.CharField(max_length = 30)
    post_dateTime = models.DateTimeField()
    def __unicode__(self):
        return self.post_title

class Comment(models.Model):
    comment_post = models.ForeignKey(Post)
    comment_text = models.CharField(max_length = 100)
    comment_dateTime = models.DateTimeField()
    def __unicode__(self):
        return self.comment_text