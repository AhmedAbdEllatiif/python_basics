from django.urls import path
from orders import views


urlpatterns = [
    path('api/orders/',views.ALLOrders.as_view()),
    path('api/orders/paid/',views.PaidOrders.as_view(),name ="paid_orders" ),
    path('api/orders/<slug>/',views.single_order,name ="order_by_id" ),
    path('api/orders/<slug>/pay',views.pay_order,name ="pay_order" ),
    path('api/orders/add-to-cart/<slug>/',views.add_to_cart,name ="add_to_cart" ),
    path('api/products/<slug>/',views.product_by_id,name ="product_by_id" ),
    path('api/orders/deletall',views.delet_all),
]

