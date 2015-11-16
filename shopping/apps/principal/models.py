from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Type_product(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length = 30)
	price = models.DecimalField(max_digits = 12, decimal_places = 5)
	type_product = models.ForeignKey(Type_product, blank = False, null = True)
	photo = models.ImageField(upload_to = 'img/product/', blank = True)
	def __str__(self):
		return self.name

class Shop_temporal(models.Model):
	user = models.ForeignKey(User, blank = False, null = True)
	product = models.ForeignKey(Product, blank = False, null = True)
	date = models.DateField(default = datetime.now)
	def __str__(self):
		return str(self.user)

class Shop_desc(models.Model):
	user = models.ForeignKey(User, blank = False, null = True)
	product = models.ForeignKey(Product, blank = False, null = True)
	def __str__(self):
		return str(self.user)