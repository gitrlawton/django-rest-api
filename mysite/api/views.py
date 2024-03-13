from django.shortcuts import render
# generics contains Generic Views
from rest_framework import generics
from.models import BlogPost
from .serializers import BlogPostSerializer

# View that gives us a way to create a new blog post, as well as 
# get all of the other blog posts that exist. We'll later need to 
# connect it to a url.
class BlogPostListCreate(generics.ListCreateAPIView):
    # Getting all of the different BlogPost objects that exist using
    # the ORM in django.
    queryset = BlogPost.objects.all()
    # Serializer we want to use when returning this data.
    serializer_class = BlogPostSerializer


# The above view utilizes the model and the serializer.
# It is a Django rest framework view.  Django rest framework provides
# default views for creating, updating, deleting and other standard
# operations.

# View that allows us to access individual posts, update them, or delete them.
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Getting all of the different BlogPost objects that exist using
    # the ORM in django.
    queryset = BlogPost.objects.all()
    # Serializer we want to use when returning this data.
    serializer_class = BlogPostSerializer
    # pk is primary key, which will be the id of the blog post.
    lookup_field = "pk"