from django.contrib import admin

# Register your models here.


# # products/admin.py
# from django.contrib import admin
# from .models import Category, Product

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent', 'is_active', 'created_at')
#     list_filter = ('is_active', 'created_at')
#     search_fields = ('name', 'description')
#     prepopulated_fields = {'name': ('name',)}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('sku', 'name', 'category', 'current_stock', 
#                    'sale_price', 'is_active', 'needs_restock')
#     list_filter = ('category', 'is_active', 'created_at')
#     search_fields = ('sku', 'name', 'barcode', 'description')
#     readonly_fields = ('created_at', 'updated_at')
#     fieldsets = (
#         ('Informações Básicas', {
#             'fields': ('sku', 'barcode', 'name', 'description', 'category')
#         }),
#         ('Preços', {
#             'fields': ('unit_cost', 'sale_price')
#         }),
#         ('Estoque', {
#             'fields': ('minimum_stock', 'current_stock')
#         }),
#         ('Status', {
#             'fields': ('is_active', 'created_at', 'updated_at')
#         }),
#     )