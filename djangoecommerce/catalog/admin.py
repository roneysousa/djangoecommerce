# coding=utf-8

from django.contrib import admin

from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'create','modified']
    search_fields = ['name','slug']
    list_filter = ['create','modified']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category','create','modified']
    search_fields = ['name','slug', 'category__name']
    list_filter = ['create','modified']


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
