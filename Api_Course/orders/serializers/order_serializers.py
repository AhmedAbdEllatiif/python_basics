from rest_framework import serializers
from orders.models import Order



class OrderSerializer(serializers.ModelSerializer):
    
    #count = serializers.IntegerField()
   
    class Meta:
        model = Order
             
      
        fields = ("id",
                  "user_id",
                  "order_num",
                  "order_status",
                  "user_commnet",
                  "products",
                  "total_amount",
                  "paid_date",
                  'paid',
                    'products_count',
                  "created_at")
        
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        