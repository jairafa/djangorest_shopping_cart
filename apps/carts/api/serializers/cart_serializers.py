from rest_framework import serializers

from apps.carts.models import Carts, CartsItems
from apps.carts.api.serializers.cart_item_serializers import CartItemSerializer, CartItemListingFielfdSerializer

class CartSerializer(serializers.ModelSerializer):
    """
    Definición de un carrito
    """

    products_items = CartItemSerializer(source='cart_to_product', many=True, read_only=True)

    class Meta:
        model = Carts
        exclude = ('state','created_date','modified_date','deleted_date')

    def create(self, validated_data):
        items_data = validated_data.pop('products_items')
        cart = Carts.objects.create(**validated_data)
        for item in items_data:
            #print (f"item {item}")
            CartsItems.objects.create(cart=cart, **item)
        return cart

