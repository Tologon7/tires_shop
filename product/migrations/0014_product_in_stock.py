# Generated by Django 5.1.6 on 2025-03-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_product_average_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
    ]
