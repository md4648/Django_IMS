# Generated by Django 5.1.6 on 2025-02-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0007_stockhistrory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StockHistrory',
            new_name='StockHistory',
        ),
    ]
