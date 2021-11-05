# Generated by Django 3.2.8 on 2021-10-26 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='cartsitems',
            name='movement',
            field=models.CharField(choices=[('+', 'Ingreso'), ('-', 'Egreso')], default='+', max_length=1, verbose_name='Movimiento(+/-)'),
        ),
        migrations.AlterField(
            model_name='historicalcartsitems',
            name='movement',
            field=models.CharField(choices=[('+', 'Ingreso'), ('-', 'Egreso')], default='+', max_length=1, verbose_name='Movimiento(+/-)'),
        ),
        migrations.AlterField(
            model_name='historicalinventory',
            name='movement',
            field=models.CharField(choices=[('+', 'Ingreso'), ('-', 'Egreso')], default='+', max_length=1, verbose_name='Movimiento(+/-)'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='movement',
            field=models.CharField(choices=[('+', 'Ingreso'), ('-', 'Egreso')], default='+', max_length=1, verbose_name='Movimiento(+/-)'),
        ),
    ]