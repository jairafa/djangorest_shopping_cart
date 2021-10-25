from django.contrib import admin

from apps.products.models import *

admin.site.register(Carts)
admin.site.register(CartsItems)
admin.site.register(Products)

