from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Category(models.Model):
    """
    A category identifier for MarketItems.
    """
    category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class MarketItem(models.Model):
    """
    A MarketItem contains product information for an item on the market.
    """
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=7, decimal_places=2, validators=[
                                     MinValueValidator(1)], default=1.00)
    item_quantity = models.PositiveIntegerField(default=1)
    # Controls if an items quantity should be frozen, AKA infinite.
    item_freeze_quantity = models.BooleanField(default=False)
    item_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Controls if an item is featured. Featured items show on the index page.
    item_is_featured = models.BooleanField(default=False)
    item_date_added = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.item_name

    class Meta:
        verbose_name = 'Market Item'
        verbose_name_plural = 'Market Items'

    def available_for_purchase(self):
        """
        Items with quantity above zero are available for purchase,
        else they are not available.
        """
        if self.item_quantity > 0:
            return True
        else:
            return False
