from django.contrib import admin
from .models import Category, Product, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  
    search_fields = ('name',)  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price') 
    list_filter = ('category',)  
    search_fields = ('name', 'category__name')  


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'created_at')  
    list_filter = ('created_at',) 
    search_fields = ('product__name',)  
