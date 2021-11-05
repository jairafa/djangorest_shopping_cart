# Generated by Django 3.2.8 on 2021-10-31 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211025_2318'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0002_auto_20211026_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='products',
        ),
        migrations.AlterField(
            model_name='carts',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='cartsitems',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.carts'),
        ),
        migrations.AlterField(
            model_name='cartsitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]