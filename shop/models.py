from datetime import *
from django.db import models
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import *
from django.utils.text import slugify


class OrderState(models.TextChoices):
    opened = 'opened'
    canceled  = 'canceled'
    delivered = 'delivered'


class Store(models.Model):
	store_admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	store_name = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	createdAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.store_name)


class Product(models.Model):
	store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
	product_name = models.CharField(max_length=100)
	price = models.FloatField()
	description = models.TextField()

	def __str__(self):
		return str(self.product_name)


class OrderItem(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"


class Order(models.Model) :
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now_add=True)
    order_state = models.CharField(max_length=30,choices=OrderState.choices,default=OrderState.opened)

    def __str__(self):
        return self.user.email    