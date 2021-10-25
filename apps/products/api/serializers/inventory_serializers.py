from rest_framework import serializers

from apps.products.models import CartsItems
#from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer

class InventorySerializer(serializers.ModelSerializer):
    """
    Definición de un producto
    """

    class Meta:
        model = Carts
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self,instance):
        return {
            'inventory_id': instance.id,
            'cart_id': instance.item.cart.id,
            'username': instance.item.cart.user.username,
            'product': instance.product.name,
            'movement': instance.movement,
            'initial_balance': instance.initial_balance,
            'quantity': instance.quantity,
            'final_balance': instance.final_balance,
            'stock': instance.product.stock,
        }
