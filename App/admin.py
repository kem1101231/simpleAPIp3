from django.contrib import admin
from django.db.models.base import Model
from .models import Movies, Inventory, Product, Purchase, PurchaseLine, Supplier, Sales, SalesLine

admin.site.register(Movies)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(PurchaseLine)
admin.site.register(Purchase)
admin.site.register(Supplier)
admin.site.register(SalesLine)
admin.site.register(Sales)