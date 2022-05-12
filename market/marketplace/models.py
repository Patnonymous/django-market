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
        return f'{self.id}: {self.category_name}'

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
    item_freeze_quantity = models.BooleanField(default=False)
    item_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_is_featured = models.BooleanField(default=False)
    item_date_added = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.item_name

    class Meta:
        verbose_name = 'Market Item'
        verbose_name_plural = 'Market Items'
