from django.contrib import admin
from .models import Category, Product, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list = ['category_name', 'description', 'created_at', 'updated_at']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list = ['Product_name', 'description', 'price', 'image', 'category', 'created_at', 'updated_at']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list = ['customer_name', 'email', 'product', 'quantity', 'created_at', 'updated_at']