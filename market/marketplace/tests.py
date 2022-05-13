from django.test import TestCase
from django.utils import timezone

from .models import MarketItem, Category


# Add helper functions here.
def quick_create_item(item_name, is_quantity_frozen, is_featured, category, description='Quick created item.', price=12.34, quantity=50):
    """
    Quickly create an item by giving a name, setting if quantity froze, and setting
    if the item is featured. All other properties will be set to some default values.
    The date will be set to current date time.
    """
    time = timezone.now()
    return MarketItem.objects.create(item_name=item_name, item_description=description, item_price=price, item_quantity=quantity, item_freeze_quantity=is_quantity_frozen, item_category_id=category, item_is_featured=is_featured, item_date_added=time)


def quick_create_cat():
    """
    Quickly create a testing category.

    """
    testing_category = Category(category_name='Tester Items Category')
    testing_category.save()
    return testing_category


# Create your tests here.
class MarketItemModelTests(TestCase):
    def test_available_to_purchase_zero_quantity(self):
        """
        available_for_purchase return False for items with quantities below 1.
        """
        # Need category FK
        testing_category = quick_create_cat()
        zero_quantity_item = quick_create_item(
            'Zero Quantity Item', False, False, testing_category, quantity=0)
        self.assertIs(zero_quantity_item.available_for_purchase(), False)

    def test_available_to_purchase_above_zero(self):
        """
        available_for_purchase return True for items with quantities above zero.
        """
        testing_category = quick_create_cat()
        five_quantity_item = quick_create_item(
            'Five Quantity Item', False, False, testing_category, quantity=5)
        self.assertIs(five_quantity_item.available_for_purchase(), True)
