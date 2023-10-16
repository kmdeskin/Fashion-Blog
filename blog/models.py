#first step is to import models from Djangos database module 
from django.db import models
#I defined a new class, blogPost, that inherits from models.Model  
class blogPost(models.Model):
    #create a title using models.CharField
    title = models.CharField(max_length=200) 
    #content serves as the body of the blog post  
    content = models.TextField() 
    pubDate = models.DateTimeField("date published")


