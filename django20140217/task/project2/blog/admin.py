__author__ = 'Artur'
from django.contrib import admin
from blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_dateTime')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_dateTime', 'comment_post', 'comment_text')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)