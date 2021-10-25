from rest_framework import serializers

from apps.products.models import Carts
#from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer

class CartSerializer(serializers.ModelSerializer):
    """
    Definición de un producto
    """

    class Meta:
        model = Carts
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'user': instance.user,
        }
