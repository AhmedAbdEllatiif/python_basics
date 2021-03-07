from django.contrib import admin
from .models import OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id","product_id","item_price","quantity","total_price")


admin.site.register(OrderItem,OrderAdmin)