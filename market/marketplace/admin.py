from django.contrib import admin

# Import models.
from .models import Category, MarketItem

# Create customized form classes for models.


class MarketItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Info', {'fields': ['item_name',
         'item_description', 'item_category_id']})
    ]

    # Customize the display in the list to show detailed information.
    list_display = ('id', 'item_name', 'item_description', 'item_price',
                    'item_quantity', 'item_freeze_quantity', 'item_category_id', 'item_is_featured', 'item_date_added')
    search_fields = ['item_name']


# Register your models here.
admin.site.register(Category)
admin.site.register(MarketItem, MarketItemAdmin)
