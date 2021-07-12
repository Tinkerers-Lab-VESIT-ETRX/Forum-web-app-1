from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list':post
    }
    return render(request,"blog_list.html",context)
    
def home(request):
    context = {
        'forum_count':Forums.objects.all().count(),
        'forums': Forums.objects.all()
    }
    return render(request,"home.html", context)

def AddForum(request):
    return render(request,"forum.html")

def AddNewForum(request):
    newForum = Forums.objects.create(
        Name = request.POST['name'],
        Email = request.POST['email'],
        Topic = request.POST['topic'],
        Description =request.POST['description'],
        Link = request.POST['link']
    )
    newForum.save()
    return redirect("/")

def ViewDiscussion(request, topic):
    forum = Forums.objects.get(Topic=topic)
    context = {
        'forum': forum,
        'comments': Discussion.objects.filter(Forum = forum)
    }
    return render(request,"discussion.html",context)

def AddDiscussion(request, topic):
    if request.method == 'GET':
        forum = Forums.objects.get(Topic=topic)
        context = {
            'forum': forum,
        }
        return render(request,"addDiscussion.html",context)
    if request.method == 'POST':
        forum = Forums.objects.get(Topic=topic)
        newDiscussion = Discussion.objects.create(
            Forum = forum,
            Name = request.POST['name'],
            Discuss = request.POST['discuss']
        )
        newDiscussion.save()
        return redirect("/Discussion/"+forum.Topic)