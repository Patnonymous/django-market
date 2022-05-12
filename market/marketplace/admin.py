from django.contrib import admin

# Import models.
from .models import Category, MarketItem

# Register your models here.
admin.site.register(Category)
admin.site.register(MarketItem)
