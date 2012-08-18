from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
	head = models.CharField(max_length=100)
	body = models.TextField(max_length=2000, null=True, blank=True)
	user_to  = models.ForeignKey(User, related_name='message_to')
	user_from = models.ForeignKey(User, related_name='message_from')
	created_date = models.DateTimeField('date created',auto_now_add=True)
	read_date = models.DateTimeField('date updated', null=True, blank=True)





	