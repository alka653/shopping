from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *

def home(request):
	categories = Type_product.objects.all()
	products = Product.objects.all().order_by('-id')[:8:1]
	title = 'Bienvenido'
	return render(request, 'shop/home.html', {'title': title, 'product_temp': '', 'categories': categories, 'products': products})

def login_user(request):
	title = 'Ingresar'
	form = LoginForm()
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
			else:
				messages.add_message(request, 40, 'Usuario inactivo')
			return HttpResponseRedirect('/')
		else:
			messages.add_message(request, 30, 'Usuario no existente')
	return render(request, 'user/login.html', {'forms': form, 'title': title})

def registry(request):
	title = 'Registrarme'
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, 25, 'Te has Registrado')
		else:
			messages.add_message(request, 30, 'Ha ocurrido un error')
		return HttpResponseRedirect('/Registrarme')
	else:
		form = RegisterForm()
	return render(request, 'user/register.html', {'forms': form, 'title': title})

def logout_user(request):
	logout(request)
	messages.add_message(request, 25, 'Exito al salir')
	return HttpResponseRedirect('/Login')

def list_producto(request, category_id):
	title = 'Lista de producto'
	product_temp = Shop_temporal.objects.filter(user = request.user)
	category = Type_product.objects.get(pk = category_id)
	products = Product.objects.filter(type_product = category_id)
	return render(request, 'shop/list_product.html', {'product_temp': product_temp, 'products': products, 'category': category, 'title': title})

@login_required(login_url = '/Login')
def add_producto(request, product_id):
	product = Product.objects.get(pk = product_id)
	shop_temporal = Shop_temporal(user = request.user, product = product)
	shop_temporal.save()
	return HttpResponseRedirect('/')

@login_required(login_url = '/Login')
def my_product(request):
	product_temp = Shop_temporal.objects.filter(user = request.user)
	title = 'Mi lista de productos'
	shop_temporal = Shop_temporal.objects.filter(user = request.user)
	return render(request, 'shop/my_list.html', {'product_temp': product_temp, 'shop_temporal': shop_temporal, 'title': title})

@login_required(login_url = '/Login')
def delete_product(request, shop):
	shopping = Shop_temporal.objects.get(pk = shop)
	shopping.delete()
	return HttpResponseRedirect('/Mis-productos/')

@login_required(login_url = '/Login')
def shopping(request):
	shopping = Shop_temporal.objects.filter(user = request.user)
	for shop in shopping:
		product = Product.objects.get(pk = shop.product.pk)
		product_temp = Shop_temporal.objects.get(user = request.user, product = shop.product.pk)
		shop_desc = Shop_desc(user = request.user, product = product)
		shop_desc.save()
		product_temp.delete()
	return HttpResponseRedirect('/Mis-compras/')

@login_required(login_url = '/Login')
def my_shop(request):
	title = 'Mi lista de productos'
	product_temp = Shop_temporal.objects.filter(user = request.user)
	shop = Shop_desc.objects.filter(user = request.user)
	return render(request, 'shop/my_shop.html', {'shop': shop, 'product_temp': product_temp, 'title': title})