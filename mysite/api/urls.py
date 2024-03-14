from django.urls import path
from . import views # . is current directory/current package

urlpatterns = [
    # Rendering our class based view we created, as a view.
    # Any time we go to the endpoint blogposts/, we'll be brought to the and
    # BlogPostListCreate view page to interact with the API.
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update")
]