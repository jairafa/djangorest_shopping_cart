from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.carts.api.serializers.cart_item_serializers import CartItemSerializer
from apps.carts.models import CartsItems


class CartsItemsViewSet(viewsets.ModelViewSet):
    """
    Consulta o actualiza un Item de un Carrito


    Características de los Items de los Carritos
    """
    serializer_class = CartItemSerializer

    def get_queryset(self, pk=None):
        print(f"CartsItemsViewSet Ingresa al get_queryset pk ({pk})")
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        """
        Retorna un listado de los items de los Carritos


        Presentación de los items a retornar de un Carrito
        """
        cart_item_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(cart_item_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        Permite la Creación de un Item de Carrito


        A continuación se describen los datos para crear un Item de Carrito
        """
        serializer = self.serializer_class(data=request.data)        
        if serializer.is_valid():
            cart_item = serializer.save()
            return Response({'cart_item':serializer.data, 'message': 'Item creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Actualización de un Item de Carrito


        A continuación se describen los datos para modificar un item de un Carrito
        """
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            cart_item_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if cart_item_serializer.is_valid():
                cart_item_serializer.save()
                return Response(cart_item_serializer.data, status=status.HTTP_200_OK)
            return Response(cart_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        """
        Eliminación de un Item de un Carrito


        Eliminación lógica de un Item de un Carrito
        """
        cart_item = self.get_queryset().filter(id=pk).first() # get instance        
        if cart_item:
            cart_item.state = False
            cart_item.save()
            return Response({'message':'Item de un Carrito eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe el Item de un Carrito con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
