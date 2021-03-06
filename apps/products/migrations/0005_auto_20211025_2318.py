# Generated by Django 3.2.8 on 2021-10-26 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211025_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartsitems',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartsitems',
            name='product',
        ),
        migrations.RemoveField(
            model_name='historicalcarts',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalcarts',
            name='user',
        ),
        migrations.RemoveField(
            model_name='historicalcartsitems',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='historicalcartsitems',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalcartsitems',
            name='product',
        ),
        migrations.RemoveField(
            model_name='historicalinventory',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalinventory',
            name='item',
        ),
        migrations.RemoveField(
            model_name='historicalinventory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='item',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='product',
        ),
        migrations.DeleteModel(
            name='Carts',
        ),
        migrations.DeleteModel(
            name='CartsItems',
        ),
        migrations.DeleteModel(
            name='HistoricalCarts',
        ),
        migrations.DeleteModel(
            name='HistoricalCartsItems',
        ),
        migrations.DeleteModel(
            name='HistoricalInventory',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
