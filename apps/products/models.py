from django.db import models

from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class Products(BaseModel):
    """Model definition for Product."""

    name = models.CharField('Nombre de Producto', max_length=150, unique = True,blank = False,null = False)
    stock = models.PositiveIntegerField('Existencia',blank = False,null = False , default=1)
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
        return f"*{self.id} {self.name}"

