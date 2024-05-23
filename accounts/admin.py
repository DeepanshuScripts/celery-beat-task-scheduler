from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display =['id','mobile_number']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display =['id','category_name']

class BrandAdmin(admin.ModelAdmin):
    list_display =['id','brand_name']

class ProductAdmin(admin.ModelAdmin):
    list_display =['id','product_name']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Product,ProductAdmin)