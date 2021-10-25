# Generated by Django 3.2.8 on 2021-10-25 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20211025_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartsitems',
            name='movement',
            field=models.CharField(default='+', max_length=1, verbose_name='Movimiento(+/-)'),
        ),
        migrations.AddField(
            model_name='historicalcartsitems',
            name='movement',
            field=models.CharField(default='+', max_length=1, verbose_name='Movimiento(+/-)'),
        ),
        migrations.AlterField(
            model_name='cartsitems',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='historicalcartsitems',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='historicalproducts',
            name='stock',
            field=models.PositiveIntegerField(default=1, verbose_name='Existencia'),
        ),
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.PositiveIntegerField(default=1, verbose_name='Existencia'),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('movement', models.CharField(default='+', max_length=1, verbose_name='Movimiento(+/-)')),
                ('initial_balance', models.PositiveIntegerField(default=0, verbose_name='Saldo Inicial')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('final_balance', models.PositiveIntegerField(default=0, verbose_name='Saldo Final')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts_products', to='products.cartsitems')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_movement', to='products.products')),
            ],
            options={
                'verbose_name': 'Item Producto',
                'verbose_name_plural': 'Items Productos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalInventory',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('movement', models.CharField(default='+', max_length=1, verbose_name='Movimiento(+/-)')),
                ('initial_balance', models.PositiveIntegerField(default=0, verbose_name='Saldo Inicial')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('final_balance', models.PositiveIntegerField(default=0, verbose_name='Saldo Final')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.cartsitems')),
                ('product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.products')),
            ],
            options={
                'verbose_name': 'historical Item Producto',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]