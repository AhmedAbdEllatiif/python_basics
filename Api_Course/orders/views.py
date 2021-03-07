#django
from django.shortcuts import render,get_object_or_404
from django.http.response import JsonResponse
from django.contrib.auth.models import User 
from django.http import HttpResponse
#datetime
from datetime import datetime
# Handle errors
from pro_utils.errors import print_error
# models
from orders.models import Order,Product,OrderItem
# Serializers
from orders.serializers.order_serializers import OrderSerializer
from orders.serializers.product_serializer import ProductSerializer
# rest_framework
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser



class ALLOrders(APIView):
  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

   
    def get(self, request, format=None):
        queryset = Order.objects.filter(user=request.user)
        serializer_class = OrderSerializer(queryset, many = True)
        return JsonResponse(status = 200,data = {"data" : serializer_class.data}, safe=False)
    
    
class PaidOrders(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
   
   
    def get(self, request, format=None):
        queryset = Order.objects.filter(user=request.user,paid=True)
        serializer_class = OrderSerializer(queryset, many = True)
        return JsonResponse(serializer_class.data,safe=False)
    
    
@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def product_by_id(request,slug):
    product_qs = Product.objects.filter(slug = slug)
    if product_qs.exists():
        order = product_qs
        
        serializer = ProductSerializer(order, many = True)
        return Response(serializer.data)
  
  
@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated,))
def single_order(request,slug):
        try:
            order_qs = Order.objects.filter(slug = slug)
            if order_qs.exists():
                order = order_qs
                
                serializer = OrderSerializer(order, many = True)
                return Response(serializer.data)
            else:
                return JsonResponse(status=404,data={'status':404,'message':'This order not found'})
        except Exception as e:
                print_error(location='orders.views >> single_order',ex = e)
                return JsonResponse(status=505 ,data={ 'status':500,'message':'Internal server Error'})
 
 
@api_view(["POST"])
@permission_classes((permissions.IsAuthenticated,))    
def add_to_cart(request,slug):
    
    # check if the product exists
    product = get_object_or_404(Product,slug=slug)
    
    #Get or Create a new order item 
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        paid=False
    )
    
    # Fliter orders by the current user and 
    order_qs = Order.objects.filter(user=request.user,paid=False)
    
    # Check if user has order and not paid yet
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order has the product already to increase its quantity
        if order.items.filter(product__slug = product.slug).exists():
            order_item.quantity += 1
            order_item.save()
            #Show message qunatity updated
            return JsonResponse(status=200, data = {'order_id': order.id,
                                                    "message" : 'Product Qunatity Updated',
                                                    'product' : str(order_item.product),
                                                    'product_quantity' :  order_item.quantity,
                                                    },safe=False)
            
        else: # Add a new order_item to the order
            order.items.add(order_item)
            #show message added to cart
            return JsonResponse(status=200, data = {'order_id': order.id,
                                                    "message" : f"New {str(order_item.product)} Added to cart",
                                                    'product' : str(order_item.product),
                                                    'quantity' : order_item.quantity,
                                                    },safe=False)
  
    else: # user has no unpaid order
        #paid_date = datetime.now()
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        #messages.info(request, "This item was added to your cart.")
        products = order.products
        return JsonResponse(status=201,
                            data={'message':'New Order Created Succssfully',
                                'order_id' : order.id,
                                'total_amount': order.total_amount,
                                'product_count': order.products_count,
                                'status':201,
                                })
      


    orders = Order.objects.filter(user_id= user_id)
    serializer = OrderSerializer(orders, many = True)
    return JsonResponse(serializer.data,safe=False)
    

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def pay_order(request,slug):
    try:
        order = Order.objects.get(user=request.user, slug=slug)
        if order.paid == True :
            return JsonResponse(status=200,data = {'message': 'Order Already paid',}) 
        else:
            paid_date = datetime.now()
            order.paid = True
            order.paid_date = paid_date
            order.save(update_fields=['paid','paid_date'])
            return JsonResponse(status=200,data = {'message': 'Order Paid Successfully',}) 
    
    except Order.DoesNotExist:
        return JsonResponse(status=404,data = {'message': 'Order Not Found'})
    
    except Exception as e:
        print_error(location="orders.views >> pay_order", ex=e)
        return JsonResponse(status=500,data = {'message': 'Internal server Error',})


@api_view(["POST"])
@permission_classes((permissions.IsAuthenticated,permissions.IsAdminUser))
def delet_all(request):
    Order.objects.all().delete()
    #OrderItem.objects.all().delete()
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many = True)
    return JsonResponse(serializer.data,safe=False)


# To Delete all orders 
# Requires to be an admin user
""" class DeletAll(APIView):
    permission_classes = [IsAdminUser]
    Order.objects.all().delete() """
    
#delete_all_orders = DeletAll.as_view()
