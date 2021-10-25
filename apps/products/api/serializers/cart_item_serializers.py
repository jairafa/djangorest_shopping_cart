from rest_framework import serializers

from apps.products.models import CartsItems
#from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    """
    Definición de un producto
    """

    class Meta:
        model = Carts
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self,instance):
        return {
            'cart_id': instance.cart.id,
            'username': instance.cart.user.username,
            'product': instance.product.name,
            'movement': instance.movement,
            'quantity': instance.quantity,
            'stock': instance.product.stock,
        }
