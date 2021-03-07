from django.db import models
from orders.models import Order 
from product.models import Product
from django.utils.translation import gettext as _


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
   
  
    @property 
    def total_price(self):
        current_product = Product.objects.get(id = self.product.id)
        price = getattr(current_product, 'price')
        return price * self.quantity
    
    @property
    def item_price(self):
        current_product = Product.objects.get(id = self.product.id)
        price = getattr(current_product, 'price')
        return price
    
    
    

    
    
    