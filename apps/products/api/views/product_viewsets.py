from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.products.models import Products


class ProductViewSet(viewsets.ModelViewSet):
    """
    Consulta o actualiza un producto


    Características de los productos
    """
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        """
        Retorna un listado de productos


        Presentación de los datos a retornar de un producto
        """
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        Permite la Creación de un producto


        A continuación se describen los datos para crear un producto
        """
        serializer = self.serializer_class(data=request.data)        
        if serializer.is_valid():
            product = serializer.save()
            return Response({'product':serializer.data, 'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Actualización de atributos de un producto


        A continuación se describen los datos para modificar un producto
        """
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        """
        Eliminación de un producto


        Eliminación lógica de un producto
        """
        product = self.get_queryset().filter(id=pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
