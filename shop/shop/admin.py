from django.contrib import admin


from django.contrib import admin
from .models import Product,Order





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'picture',)
    list_editable = ('price',)