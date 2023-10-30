from django.contrib import admin

# Register your models here.
from .models import Product, Orders, OrderUpdate, Credentials

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Credentials)