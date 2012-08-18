from django import forms
from django.contrib.auth.models import User

class CreateMessage(forms.Form):
	user_to = forms.CharField(label='To:', widget=forms.TextInput)
	head = forms.CharField(required=False, widget=forms.TextInput)
	body = forms.CharField(required=False, widget=forms.Textarea)

	def clean_user_to(self):
		username = self.cleaned_data['user_to']
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError(u'Sorry, that username does not exist.' )
		return username
		
class DeleteMessage(forms.Form):
	message_id = forms.IntegerField(widget=forms.HiddenInput)