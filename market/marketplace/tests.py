from django.test import TestCase
from django.utils import timezone

from .models import MarketItem, Category


# Add helper functions here.
def quick_create_item(item_name, is_quantity_frozen, is_featured, description='Quick created item.', price=12.34, quantity=50, category=1):
    """
    Quickly create an item by giving a name, setting if quantity froze, and setting
    if the item is featured. All other properties will be set to some default values.
    The date will be set to current date time.
    """
    time = timezone.now()
    return MarketItem.objects.create(item_name=item_name, item_description=description, item_price=price, item_quantity=quantity, item_freeze_quantity=is_quantity_frozen, item_category_id=category, item_is_featured=is_featured, item_date_added=time)


# Create your tests here.
class MarketItemModelTests(TestCase):
    def test_available_to_purchase_zero_quantity(self):
        """
        available_for_purchase return False for items with quantities below 1.
        """
        zero_quantity_item = quick_create_item(
            'Zero Quantity Item', False, False, quantity=0)
        self.assertIs(zero_quantity_item.available_for_purchase(), False)
