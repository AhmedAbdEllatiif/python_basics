from rest_framework import serializers
from .models import Post
from django import forms
from rest_framework.fields import CurrentUserDefault
     
class PostSerializers(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner',
            "timestamp"
            )

      
        

        
