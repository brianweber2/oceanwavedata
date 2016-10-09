from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class UserProfileInline(admin.StackedInline):
	model = models.UserProfile
	can_delete = False


class UserAdmin(admin.ModelAdmin):
	search_fields = ['username', 'email', 'first_name', 'last_name']

	list_display = ['username', 'first_name', 'last_name', 'display_name',
	'email', 'is_active', 'is_staff']

	list_filter = ['is_active', 'is_staff', 'date_joined']

	list_editable = []

	inlines = (UserProfileInline,)

	# fieldsets = (
	# 	(None, {'fields': ('username', 'password')}),
	# 	('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
	# 	('Permissions', {'fields': ('is_active', 'is_staff')}),
	# 	('Groups', {'fields': ('groups')}),
	# )

admin.site.register(models.User, UserAdmin)