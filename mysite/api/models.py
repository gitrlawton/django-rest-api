from django.db import models

# Create your database models here.
# Django uses an ORM (Object Relational Mapping) - a higher level
# python wrapper - which maps a python object to a database instance.

# This class will inherit from the database model class.
class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    # auto_now_add automatically fills in the published_date for us.
    published_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title
    
    