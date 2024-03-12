# A serializer is a class that will take our database model 
# and transform it into json compatible data.

from rest_framework import serializers
from .models import BlogPost

# This class inherits from the ModelSerializer class.
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # Fields we would like to serialize and return.  These are
        # all the fields in our BlogPost class. Id needs to be included
        # here as something we want to serialize, even if it isn't
        # a field we explicitly lay out in the BlogPost class (it is
        # automatically generated for us in there.)
        fields = ["id", "title", "content", "published_date"]