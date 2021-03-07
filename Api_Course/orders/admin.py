from django.contrib import admin
from .models import Order
from .models import OrderItem , Product,ProductImage



class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_num","paid","created_at","user")
    list_filter  = ['order_num','paid','user',]




class ProductImageAdmin(admin.StackedInline):
    model = ProductImage



class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","title",)
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product
       
    

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id","product_id","item_price","quantity","total_price")
   






admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Product,ProductAdmin)
