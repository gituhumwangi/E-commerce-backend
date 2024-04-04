from django.contrib import admin
from .models import Product, Order, UserProfile, OrderItem, Review

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
#admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(OrderItem)
admin.site.register(Review)
