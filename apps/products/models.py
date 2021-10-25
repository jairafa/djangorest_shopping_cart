from django.db import models

from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.users.models import User

class Products(BaseModel):
    """Model definition for Product."""

    name = models.CharField('Nombre de Producto', max_length=150, unique = True,blank = False,null = False)
    stock = models.IntegerField('Existencias', default=0)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name


class Carts(BaseModel):
    """Model definition for Product."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Cliente',blank = False, null = False)
    products = models.ManyToManyField(Products, verbose_name = 'Productos Carrito', through='CartsItems', related_name = 'items' )
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
        return  f'{self.user} Carrito {self.id}'


class CartsItems(BaseModel):
    """Model definition for Product."""
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE,blank = False, null = False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE,blank = False, null = False)
    quantity = models.IntegerField('Cantidad', default=0)
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
        return  f'{self.user} Carrito {self.id}'
