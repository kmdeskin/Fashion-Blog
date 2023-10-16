#render function is used to render HTML templates and return an HTTP response with the rendered content
from django.shortcuts import render
#import blogPost model from models.py
from .models import blogPost

#blogpostList takes request and returns a web response 
def blog_post_list(request):
    #queries database to retrieve all posts 
    posts = blogPost.objects.all()
    #path to the HTML template used to render the response 
    return render(request, 'blog/blog_post_list.html', {'posts': posts})
