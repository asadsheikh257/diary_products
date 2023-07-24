from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.db.models import Count
from . forms import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def Home(request):
    context = {'page':'Dairy Products | Home'}
    return render(request, 'app/home.html', context)

def About(request):
    context = {'page':'Dairy Products | About'}
    return render(request, 'app/about.html', context)

def Contact(request):
    context = {'page':'Dairy Products | Contact Us'}
    return render(request, 'app/contact.html', context)


def Category(request, val):
    product = Product.objects.filter(category=val)
    title = Product.objects.filter(category=val).values('title')
    context = {'page': 'Category Product', 'val':val, 'product':product, 'title':title}
    return render(request, 'app/category.html', context)  

  
def CategoryTitle(request, val):
    product = Product.objects.filter(title=val)
    title = Product.objects.filter(category=product[0].category).values('title')
    context = {'page' : val.title, 'product':product, 'title':title, 'val':val }
    return render(request, 'app/category.html', context)   
 

def ProductDetail(request, id):
    queryset = Product.objects.get(id = id)
    context = {'page': 'Product Detail', 'product': queryset}
    return render (request,'app/product_detail.html',context)


def CustomerRegistrationView(request):
    form =  CustomerRegistrationForm()
    if (request.method == "POST"):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
    context = {'page':'Customer Registration', 'form':form}
    return render(request, 'app/registration.html', context)
    

def ProfileView(request):
    form = CustomerProfileForm()
    if (request.method == "POST"):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            Customer.objects.create(
                user = user,
                name = name,
                locality = locality,
                city = city,
                mobile = mobile,
                state = state,
                zipcode = zipcode
            )
            messages.success(request, "Congratulations! Profile save successfully")
        else:
            messages.warning(request, "Invalid Data Input")
    context = {'page':'Profile', 'form':form}
    return render(request, 'app/profile.html', context)


def AddressView(request):
    add = Customer.objects.filter(user=request.user)
    context = {'page' : "Address", 'add' : add}
    return render(request, 'app/address.html',context)


def UpdateAddress(request, id):
    address = Customer.objects.get(id=id)
    queryset = CustomerProfileForm(instance=address)

    if(request.method == "POST"):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            address = Customer.objects.get(id = id)
            address.name = form.cleaned_data['name']
            address.locality = form.cleaned_data['locality']
            address.city = form.cleaned_data['city']
            address.mobile = form.cleaned_data['mobile']
            address.state = form.cleaned_data['state']
            address.zipcode = form.cleaned_data['zipcode']

            address.save()
            messages.success(request,'Congratulations! Profile Updated Successfully')
        else:
            messages.warning(request, 'Input Data Invalid')
        return redirect('address')

    context = {'page':'Update Address', 'address':address, 'queryset':queryset}
    return render(request, 'app/updateAddress.html', context)


def AddToCart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def ShowCart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value =  p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'app/add_to_cart.html', locals())


def Plus_Cart(request):
    if request.method != 'GET':
        return
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        amount = amount + p.quantity * p.product.discounted_price
    totalamount = amount + 40
    data = {
        'quantity': c.quantity,
        'amount' : amount,
        'totalamount' : totalamount
     }
    return JsonResponse(data)


def Minus_Cart(request):
    if request.method != 'GET':
        return
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        amount = amount + p.quantity * p.product.discounted_price
    totalamount = amount + 40
    data = {
        'quantity': c.quantity,
        'amount' : amount,
        'totalamount' : totalamount
     }
    return JsonResponse(data)

def Remove_Cart(request):
    if request.method != 'GET':
        return
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        amount = amount + p.quantity * p.product.discounted_price
    totalamount = amount + 40
    data = {
        'quantity': c.quantity,
        'amount' : amount,
        'totalamount' : totalamount
     }
    return JsonResponse(data)

