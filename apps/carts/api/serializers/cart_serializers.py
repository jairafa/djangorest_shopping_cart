from rest_framework import serializers

from apps.carts.models import Carts, CartsItems
from apps.carts.api.serializers.cart_item_serializers import CartItemSerializer

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


    def update(self, instance, validated_data):
        items_data = self.initial_data.get("products_items")

        for item in items_data:
            product_id = item.get("product")
            quantity = item.get("quantity")
            movement = item.get("movement")
            obj, created = CartsItems.objects.update_or_create(
                cart_id = instance.id, product_id = product_id, quantity=quantity,movement=movement)
            #if created:            
        return instance
