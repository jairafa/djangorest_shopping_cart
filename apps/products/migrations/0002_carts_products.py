# Generated by Django 3.2.8 on 2021-10-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='products',
            field=models.ManyToManyField(related_name='items', through='products.CartsItems', to='products.Products', verbose_name='Productos Carrito'),
        ),
    ]
