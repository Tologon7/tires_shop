# Generated by Django 5.1.6 on 2025-03-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_rename_quantity_product_instock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
