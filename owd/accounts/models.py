from __future__ import unicode_literals

from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin
)
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings

from django_countries.fields import CountryField
from smartfields import fields


class UserManager(BaseUserManager):
	def create_user(self, first_name, last_name, email, username=None,
					display_name=None, password=None):
		if not first_name:
			raise ValueError("Please provide your first name.")
		if not last_name:
			raise ValueError("Please provide your last name.")
		if not email:
			raise ValueError("Users must have an email address.")
		if not username:
			username = email.split('@')[0]
		if not display_name:
			display_name = first_name.capitalize()

		user = self.model(
			first_name=first_name,
			last_name=last_name,
			email=self.normalize_email(email),
			username=username,
			display_name=display_name
		)

		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, first_name, last_name, email, username, 
						display_name, password):
		user = self.create_user(
			first_name,
			last_name,
			email,
			username,
			display_name,
			password
		)
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	username = models.CharField(max_length=40, unique=True)
	display_name = models.CharField(max_length=140)
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["first_name", "last_name", "display_name", "username"]

	def __str__(self):
		return "@{}".format(self.username)

	def get_short_name(self):
		return self.display_name

	def get_long_name(self):
		return "{} (@{})".format(self.display_name, self.username)


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	company = models.CharField(max_length=40, blank=True, default="")
	position = models.CharField(max_length=40, blank=True, default="")
	bio = models.CharField(max_length=300, blank=True, default="")
	avatar = fields.ImageField(blank=True, null=True)
	location = models.CharField(max_length=40, blank=True, default="")
	country = CountryField(blank=True, default="")
	billing_address = models.TextField(blank=True, default="")

	def get_absolutel_url(self):
		return reverse("accounts:profile", {'username': self.username})


def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
