from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse 


def delete_product(request, id):
    products = get_object_or_404(Product, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_product(request, id):
    news = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=news)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_json_by_id(request, products_id):
  # GANTI fungsi show_json_by_id lama kamu dengan ini
    try:
        p = Product.objects.select_related('user').get(pk=products_id)
        data = {
            "id": p.id,  # int
            "name": p.name,
            "description": p.description,
            "price": p.price,
            "category": p.category,                     
            "thumbnail": p.thumbnail,
            "products_views": p.products_views,
            "is_featured": p.is_featured,
            "is_products_hot": p.is_products_hot,       
            "user_id": p.user.id,
            "user_username": p.user.username if p.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)


def show_xml_by_id(request, products_id):
   try:
       products_item = Product.objects.filter(pk=products_id)
       xml_data = serializers.serialize("xml", products_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)


def show_json_by_id(request, products_id):
   products_item = Product.objects.get(pk=products_id)
   json_data = serializers.serialize("json", [products_item])
   return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
   products_item = Product.objects.filter(pk=products_id)
   xml_data = serializers.serialize("xml", products_item)
   return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'id': str(products.id),
            'title': products.name,
            'content': products.content,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'news_views': products.news_views,
            'created_at': products.created_at.isoformat(), #if products.created_at else None,
            'is_featured': products.is_featured,
            'user_id': products.user_id,
        }
        for products in products_list
    ]

    return JsonResponse(data, safe=False)

def show_xml(request):
    products_list = Product.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

@login_required(login_url='/login')
def show_main(request):
    products_list = Product.objects.all()

    context = {
        'name': 'Theo Samuel',
        'class': 'PBP A',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

@login_required(login_url='/login')
def show_products(request, id):
    products = get_object_or_404(Product, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "show_products.html", context)