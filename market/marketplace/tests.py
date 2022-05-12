from django.test import TestCase
from django.utils import timezone

from .models import MarketItem, Category


# Add helper functions here.
def quick_create_item(item_name, is_quantity_frozen, is_featured):
    """
    Quickly create an item by giving a name, setting if quantity froze, and setting
    if the item is featured. All other properties will be set to some default values.
    The date will be set to current date time.
    """
    time = timezone.now()
    return MarketItem.objects.create(item_name=item_name, item_description='Quick created item.', item_price=12.34, item_quantity=50, item_freeze_quantity=is_quantity_frozen, item_category_id=1, item_is_featured=is_featured, item_date_added=time)
# Create your tests here.
