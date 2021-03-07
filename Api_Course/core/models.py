from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField( max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    



    
    def __str__(self):
        return self.title
    
