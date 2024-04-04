from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Order, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# View to display a list of products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# View to display product details
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

# View to handle user registration
def user_registration(request):
    # Your registration logic here
    return HttpResponse("User registration page")

# View to handle user login
def user_login(request):
    # Your login logic here
    return HttpResponse("User login page")

# View to display shopping cart
@login_required
def shopping_cart(request):
    user_profile = UserProfile.objects.get(user=request.user)
    order = Order.objects.filter(user_profile=user_profile, status='pending').first()
    return render(request, 'shopping_cart.html', {'order': order})

# View to handle checkout
@login_required
def checkout(request):
    # Your checkout logic here
    return HttpResponse("Checkout page")

# View to display order history
@login_required
def order_history(request):
    orders = Order.objects.filter(user_profile__user=request.user)
    return render(request, 'order_history.html', {'orders': orders})
