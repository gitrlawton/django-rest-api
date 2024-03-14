from django.shortcuts import render
# generics contains Generic Views
from rest_framework import generics, status
from rest_framework.response import Response
from.models import BlogPost
from .serializers import BlogPostSerializer
# For creating custom API views.
from rest_framework.views import APIView

# View that gives us a way to create a new blog post, as well as 
# get all of the other blog posts that exist. We'll later need to 
# connect it to a url.
class BlogPostListCreate(generics.ListCreateAPIView):
    # Getting all of the different BlogPost objects that exist using
    # the ORM in django.
    queryset = BlogPost.objects.all()
    # Serializer we want to use when returning this data.
    serializer_class = BlogPostSerializer
    
    # Defining our own route to override the default ListCreateAPIView
    # view.  Creates a Delete button for deleting blog posts.
    def delete(self, request, *args, **kwargs):
        # Delete all the blog posts that exist.
        BlogPost.objects.all().delete()
        # Return status for content deleted.
        return Response(status = status.HTTP_204_NO_CONTENT)

# The above view utilizes the model and the serializer.
# It is a Django rest framework view.  Django rest framework provides
# default views for creating, updating, deleting and other standard
# operations.  You can override them.


# View that allows us to access individual posts, update them, or delete them.
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # Getting all of the different BlogPost objects that exist using
    # the ORM in django.
    queryset = BlogPost.objects.all()
    # Serializer we want to use when returning this data.
    serializer_class = BlogPostSerializer
    # pk is primary key, which will be the id of the blog post.
    lookup_field = "pk"
    
# Custom API view.  Making our own routes in the case we don't want to
# use the generic ones.  It needs to be added to urlpatterns in urls.py
# as views.BlogPostList.as_view()
class BlogPostList(APIView):
    # A route for the GET method.
    def get(self, request, format = None):
        # Get the title from the query parameters (if none, default to
        # an empty string).
        title = request.query_params.get("title", "")
        
        if title:
            # Filter the queryset based on the title.
            blog_posts = BlogPost.objects.filter(title_icontains = title)
        else:
            # If no title is provided, return all blog posts.
            blog_posts = BlogPost.objects.all()
            
        # Serialize the blog posts.
        serializer = BlogPostSerializer(blog_posts, many = True)
        # Response containing the data from the serializer, plus the status.
        return Response(serializer.data, status = status.HTTP_200_OK)
            
            