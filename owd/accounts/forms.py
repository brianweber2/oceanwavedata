from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.models import model_to_dict, fields_for_model

from django_countries import widgets, countries
from smartfields import fields

from . import models


User = get_user_model()

class UserCreateForm(UserCreationForm):
	username = forms.CharField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	first_name = forms.CharField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'First name'}))
	last_name = forms.CharField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
	email = forms.CharField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
	password1 = forms.CharField(label="", help_text="", 
		widget=forms.PasswordInput(attrs={'placeholder': 'Create password'}))
	password2 = forms.CharField(label="", help_text="", 
		widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation'}))

	class Meta:
		fields =(
			"username",
			"first_name", 
			"last_name",
			"email", 
			"password1", 
			"password2"
		)
		model = get_user_model()


class UserProfileUpdateForm(forms.ModelForm):
	company = forms.CharField(max_length=40)
	position = forms.CharField(max_length=40)
	bio = forms.CharField(max_length=300, label='About You', widget=forms.Textarea(attrs={'rows': 6}))
	avatar = fields.ImageField(blank=True)
	location = forms.CharField(max_length=40)
	country = forms.ChoiceField(widget=widgets.CountrySelectWidget, choices=countries)
	billing_address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

	class Meta:
		model = models.UserProfile
		fields = ['avatar', 'bio', 'company', 'position', 'billing_address', 'country', 
				  'location']
		labels = {
			'avatar': _('Your Photo'),
		}


class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
		labels = {
			'email': _('Email Address'),
		}