from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product_detail', views.product_detail, name='product_detail'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('order_history', views.order_history, name='order_history'),
]