# Generated by Django 4.0.4 on 2022-05-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_alter_category_options_alter_marketitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketitem',
            name='item_date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
