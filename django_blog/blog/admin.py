from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Post)
class ForumDB(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Topic', 'Description', 'Link',)
admin.site.register(Forums, ForumDB)

class DiscussionDB(admin.ModelAdmin):
    list_display = ('Name', 'Discuss', 'Forum',)
admin.site.register(Discussion, DiscussionDB)