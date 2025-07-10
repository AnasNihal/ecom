from django.contrib import admin
from .models import Product,category,Order,OrderItem
# Register your models here.
admin.site.register(Product)
admin.site.register(category)  
admin.site.register(Order)
admin.site.register(OrderItem)       

