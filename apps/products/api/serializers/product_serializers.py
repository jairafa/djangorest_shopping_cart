from rest_framework import serializers

from apps.products.models import Products
#from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):
    """
    Definición de un producto
    """

    class Meta:
        model = Products
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,
        }
