from django.db import models

from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.products.models import Products
from apps.users.models import User

class Carts(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Cliente', null = True)
    products_items = models.ManyToManyField(Products, verbose_name = 'Productos Carrito', through='CartsItems')

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
        return  f'*{self.user} Carrito {self.id}'


class CartsItems(BaseModel):
    """Model definition for Product."""
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE,related_name='cart_to_product')
    product = models.ForeignKey(Products, on_delete=models.CASCADE,related_name='product_to_cart')
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

        verbose_name = 'Item Producto'
        verbose_name_plural = 'Items Productos'

    def __str__(self):
        return  f'*Item {self.id} Carrito {self.cart} product {self.product} quantity {str(self.quantity)} movement {self.movement}'

