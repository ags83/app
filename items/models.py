from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
	
class Item(models.Model):
	name = models.CharField(max_length=200)
	desc = models.TextField(max_length=1000, null=True, blank=True)
	image  = models.ImageField(upload_to = 'photos/', null=True, blank=True)
	category = models.CharField(max_length=50)
	price = models.CharField(max_length=100, null=True, blank=True)
	user =  models.ForeignKey(User)
	lat = models.FloatField()
	long = models.FloatField()
	created = models.DateTimeField('date created',auto_now_add=True)
	updated = models.DateTimeField('date updated',auto_now=True)
	
