from rest_framework import serializers
from orders.models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product 
        fields = [
            'id',
            'title',
            'description',
            'rate',
            'images',
        ]
