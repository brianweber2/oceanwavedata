from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from . import forms
from . import models

User = get_user_model()

class LoginView(generic.FormView):
	form_class = AuthenticationForm
	success_url = reverse_lazy('home')
	template_name = "accounts/login.html"

	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		return form_class(self.request, **self.get_form_kwargs())

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super().form_valid(form)


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


class SignUpView(SuccessMessageMixin, generic.CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy("login")
	template_name = "accounts/signup.html"
	success_message = "Your profile has been successfully created. Please log into your account."


class UserProfileView(LoginRequiredMixin, generic.DetailView):
	model = models.UserProfile
	template_name = "accounts/profile.html"
	slug_field = "user__username"
	slug_url_kwarg = 'username'


class UserProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
	model = User
	template_name = "accounts/update_profile.html"
	slug_field = "username"
	slug_url_kwarg = 'username'
	form_class = forms.UserUpdateForm
	second_form_class = forms.UserProfileUpdateForm

	# Allow two forms to be shown in the view
	def get_context_data(self, **kwargs):
		context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(instance=self.request.user)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(instance=self.request.user.userprofile)
		return context

	# Make sure both models are saved on POST
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.form_class(request.POST, instance=request.user)
		form2 = self.second_form_class(request.POST, request.FILES, instance=request.user.userprofile)

		if form.is_valid() and form2.is_valid():
			userdata = form.save(commit=False)
			userdata.save()
			profiledata = form2.save(commit=False)
			profiledata.user = userdata
			profiledata.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(
				self.get_context_data(form=form, form2=form2)
			)

	def get(self, request, *args, **kwargs):
		super(UserProfileUpdateView, self).get(request, *args, **kwargs)
		form = self.form_class(instance=request.user)
		form2 = self.second_form_class(instance=request.user.userprofile)
		return self.render_to_response(
				self.get_context_data(object=self.object, form=form, form2=form2)
			)

	def get_success_url(self):
		messages.success(self.request, 'Your profile has been successfully updated.')
		return reverse("accounts:profile", 
						kwargs={'username': self.request.user.username})