# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import *
from django import forms
from .models import *

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Usuario', widget = forms.TextInput(attrs = {'placeholder': 'Ingrese su usuario'}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder': 'Ingrese su contraseña'}), label = 'Contraseña')

class RegisterForm(forms.Form):
	first_name = forms.CharField(label = 'Nombres', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese su nombre'}))
	last_name = forms.CharField(label = 'Apellidos', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese sus apellidos'}))
	email = forms.EmailField(label = 'Correo Electrónico', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese su correo electrónico', 'type': 'email'}))
	username = forms.CharField(label = 'Usuario', widget = forms.TextInput(attrs = {'required': True, 'placeholder': 'Ingrese un usuario'}))
	password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(attrs = {'required': True, 'placeholder': 'Ingrese una contraseña'}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username = username).exists():
			raise forms.ValidationError('El usuario '+username+' ya se encuentra en uso, por favor ingrese uno nuevo')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError('El email '+email+' ya se ecuentra en uso.')
		return email

	def save(self):
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = User.objects.create_user(username, email, password)
		user.first_name = first_name
		user.last_name = last_name
		user.save()