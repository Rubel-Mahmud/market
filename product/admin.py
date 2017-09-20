from django.contrib import admin

from .models import Product, Choice

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['product', 'brand']

admin.site.register(Product, ProductAdmin)
admin.site.register(Choice, ChoiceAdmin)
