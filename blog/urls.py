#this file consists of my URLs for my blog app 
#import path to define URL patters 
from django.urls import path
#import views 
from . import views
#i created a new list to store my URL patters 
urlpatterns = [
    path('posts/', views.blog_post_list, name='blog_post_list'),
]