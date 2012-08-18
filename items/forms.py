from django import forms
from django.forms.models import model_to_dict
from models import Item

CATEGORY_CHOICES = (('accomodation', ''),
                            ('motoring', ''),
                            ('electronics', ''),
							('boating', ''),
                            ('people', ''),
							('householdgoods', ''),
                            ('sporting', ''),
							('baby', ''),
                            ('music', ''),
							)
							
#class CreateForm(forms.Form):
#    category = forms.ChoiceField(required=True, label="Category", choices= CATEGORY_CHOICES, initial='accomodation', widget=forms.RadioSelect(attrs={'class':'category-list'}))
#    lat = forms.CharField(required=True, widget=forms.HiddenInput)
#    long = forms.CharField(required=True, widget=forms.HiddenInput)
#    name = forms.CharField(required=True)
#    desc = forms.CharField(required=False, widget=forms.Textarea)
#    image = forms.FileField(required=False, label='Select an image ')
class CreateForm(forms.ModelForm):
    category = forms.ChoiceField(required=True, label="Category", choices= CATEGORY_CHOICES, initial='accomodation', widget=forms.RadioSelect(attrs={'class':'category-list'}))
    class Meta:
        model=Item
        exclude=('user',)
		
class SearchForm(forms.Form):
    category = forms.ChoiceField(required=False, label="Category", choices= CATEGORY_CHOICES, initial='accomodation', widget=forms.RadioSelect(attrs={'class':'category-list'}))
    lat = forms.FloatField(required=False, widget=forms.HiddenInput)
    long = forms.FloatField(required=False, widget=forms.HiddenInput)
    searcharea = forms.FloatField(required=False, widget=forms.HiddenInput)
	 
class EditForm(forms.ModelForm):
    class Meta:
        model=Item
        exclude=('user',)