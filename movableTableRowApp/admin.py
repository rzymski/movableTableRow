from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'position')
    list_filter = ('id', 'name', 'price', 'quantity', 'position')
    search_fields = ('id', 'name', 'price', 'quantity', 'position')
    ordering = ('id', 'name', 'price', 'quantity', 'position')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["position"].required = False
        return form

    def save_model(self, request, obj, form, change):
        if not obj.position:
            max_position = Product.objects.aggregate(models.Max('position'))['position__max']
            obj.position = max_position + 1 if max_position is not None else 1
        super().save_model(request, obj, form, change)
