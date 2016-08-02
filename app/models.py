from django.db import models
from django.contrib import admin

class Region(models.Model):
	"""Модель регионов"""
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name

class Client(models.Model):
	"""Модель заказчиков"""
	name = models.CharField(max_length=150)
	regions = models.ManyToManyField(Region)

	def __str__(self):
		return self.name		

class Provider(models.Model):
	"""Модель поставщиков"""
	name = models.CharField(max_length=150)
	regions = models.ManyToManyField(Region)

	def __str__(self):
		return self.name		

admin.site.register(Region)
admin.site.register(Client)
admin.site.register(Provider)