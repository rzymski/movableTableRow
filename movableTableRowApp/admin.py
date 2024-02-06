from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'position')
    list_filter = ('id', 'name', 'price', 'quantity', 'position')
    search_fields = ('id', 'name', 'price', 'quantity', 'position')
    ordering = ('id', 'name', 'price', 'quantity', 'position')
