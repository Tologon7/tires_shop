# Generated by Django 4.2.9 on 2024-03-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tires', '0004_rename_name_category_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tires',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]