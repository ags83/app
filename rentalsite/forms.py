from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'John123'}), max_length=14, min_length=4)
	email = forms.EmailField(label='Email',required=False, widget=forms.TextInput(attrs={'placeholder': 'myemail@email.com'}), max_length=30)
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'secret_123'}),max_length=14, min_length=6)
	password_repeat = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'placeholder': 'secret_123'}),max_length=14, min_length=6)
	
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(u'Sorry, this username is allready in use.' )
		
	def clean_password(self):
		if self.data['password'] != self.data['password_repeat']:
			raise forms.ValidationError('Passwords do not match')
		return self.data['password']