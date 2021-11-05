from rest_framework import serializers

from apps.carts.models import CartsItems
#from apps.carts.api.serializers.cart_serializers import CartSerializer



class CartItemSerializer(serializers.ModelSerializer):

    cart=serializers.StringRelatedField()
    products=serializers.StringRelatedField()

    class Meta:
        model = CartsItems
        exclude = ('state','created_date','modified_date','deleted_date')
        
