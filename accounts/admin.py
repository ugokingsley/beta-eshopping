from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class UserAdmin(ImportExportModelAdmin):
	list_display = ('username','email','is_staff','is_active','date_joined')
	list_filter = ('is_staff','is_active')
	search_fields = ['is_active']
admin.site.register(User, UserAdmin)
