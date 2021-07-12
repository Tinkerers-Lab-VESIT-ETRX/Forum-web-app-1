from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name = "home"),
    path('AddForum', AddForum, name = "AddForum"),
    path('AddNewForum', AddNewForum, name = "AddNewForum"),
    path('Discussion/<topic>', ViewDiscussion, name = "ViewDiscussion"),
    path('Discussion/<topic>/AddDiscussion', AddDiscussion, name = "AddDiscussion"),
    


    path('blog',blog_list),
]