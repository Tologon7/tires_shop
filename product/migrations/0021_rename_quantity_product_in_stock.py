# Generated by Django 5.1.6 on 2025-03-05 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_remove_product_in_stock_remove_product_set'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='in_stock',
        ),
    ]
