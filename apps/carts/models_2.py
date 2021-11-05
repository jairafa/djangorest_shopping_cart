from django.db import models

from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.products.models import Products
from apps.users.models import User

class Carts(BaseModel):
    """Model definition for Product."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Cliente',blank = False, null = False)
    #products_items = models.ManyToManyField(Products, verbose_name = 'Productos Carrito', through='CartsItems' )
    #items
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Carrito de Compras'
        verbose_name_plural = 'Carritos de Compras'

    def __str__(self):
        """Unicode representation of Product."""
        return  f'*{self.user} Carrito {self.id}'


class CartsItems(BaseModel):
    """Model definition for Product."""
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE,blank = True, null = True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE,blank = True, null = True)
    quantity = models.PositiveIntegerField('Cantidad', default=0)
    movement = models.CharField('Movimiento(+/-)', max_length=1, blank = False,null = False, 
        default='+', choices=(('+', 'Ingreso',), ('-', 'Egreso',)))
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Item Producto'
        verbose_name_plural = 'Items Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return  f'*Item {self.id} Carrito {self.cart} {self.product}  '


class Inventory(BaseModel):
    """Model definition for Product."""
    item = models.ForeignKey(CartsItems, on_delete=models.CASCADE,blank = False, null = False, related_name='carts_products')
    product = models.ForeignKey(Products, on_delete=models.CASCADE,blank = False, null = False, related_name='products_movement')
    movement = models.CharField('Movimiento(+/-)', max_length=1, blank = False,null = False, 
            default='+', choices=(('+', 'Ingreso',), ('-', 'Egreso',)))
    initial_balance = models.PositiveIntegerField('Saldo Inicial', default=0)
    quantity = models.PositiveIntegerField('Cantidad', default=0)
    final_balance = models.PositiveIntegerField('Saldo Final', default=0)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Item Producto'
        verbose_name_plural = 'Items Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return  f'*Inventory {self.id} Item {self.item} '

