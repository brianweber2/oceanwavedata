from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from . import forms

# from mpl_toolkits.basemap import Basemap
# import numpy as np 
# import matplotlib.pyplot as plt 
# import netCDF4


class Home(TemplateView):
	template_name = "home_1.html"

def about(request):
	context = {}
	template = "about.html"
	return render(request, template, context)

def projects(request):
	context = {}
	template = "projects.html"
	return render(request, template, context)

def forum(request):
	context = {}
	template = "forum.html"
	return render(request, template, context)

def blog(request):
	context = {}
	template = "blog.html"
	return render(request, template, context)

def contact_view(request):
	contact_form = forms.ContactForm()
	if request.method == 'POST':
		contact_form = forms.ContactForm(request.POST)
		if contact_form.is_valid():
			send_mail(
				'{subject}'.format(**contact_form.cleaned_data),
				'{message}'.format(**contact_form.cleaned_data),
				'{name} <{email}>'.format(**contact_form.cleaned_data),
				['brianweber2@gmail.com'] #to email
			)
			messages.success(request, 'Thanks for reaching out!')
			return HttpResponseRedirect(reverse('contact'))
	context = {'contact_form': contact_form}
	template = "contact.html"
	return render(request, template, context)
