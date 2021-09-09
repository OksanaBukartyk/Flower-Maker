from django.contrib import admin
from .models import Product,Profile,Response,Version, Category, Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Response)
admin.site.register(Version)
admin.site.register(Category)
admin.site.register(Order)