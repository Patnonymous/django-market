# Generated by Django 4.0.4 on 2022-05-11 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_marketitem_item_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketitem',
            name='item_date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
