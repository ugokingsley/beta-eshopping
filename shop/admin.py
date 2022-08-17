from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class StoreAdmin(ImportExportModelAdmin):
	list_display = ('id','store_admin','store_name','address')
	list_filter = ('store_name',)
	search_fields = ['store_name']
admin.site.register(Store, StoreAdmin)

class ProductAdmin(ImportExportModelAdmin):
	list_display = ('store','product_name','price')
	list_filter = ('store',)
	search_fields = ['store']
admin.site.register(Product, ProductAdmin)

class OrderItemAdmin(ImportExportModelAdmin):
	list_display = ('product','quantity')
	list_filter = ('product',)
	search_fields = ['product']
admin.site.register(OrderItem, OrderItemAdmin)


class OrderAdmin(ImportExportModelAdmin):
	list_display = ('store','user','order_date','order_state')
	list_filter = ('store',)
	search_fields = ['store']
admin.site.register(Order, OrderAdmin)
