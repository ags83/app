from django import forms
from django.forms.models import model_to_dict
							
class LoginForm(forms.Form):
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=14, min_length=4)
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),max_length=14, min_length=6)
