from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.carts.api.serializers.inventory_serializers import InventorySerializer
from apps.carts.models import Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    """
    Consulta o actualiza un Inventario


    Características de los Inventarios
    """
    serializer_class = InventorySerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        """
        Retorna un listado de los movimientos de los productos en los Inventarios


        Presentación de los movimientos a retornar de un Inventario de un producto
        """
        inventory_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(inventory_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        Permite la Creación de un Movimiento de Inventario


        A continuación se describen los datos para crear un Movimiento de Inventario
        """
        serializer = self.serializer_class(data=request.data)        
        if serializer.is_valid():
            inventory = serializer.save()
            return Response({'inventory':serializer.data, 'message': 'Inventario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Actualización de un Movimiento de Inventario


        A continuación se describen los datos para modificar un movimiento de un Inventario
        """
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            inventory_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if inventory_serializer.is_valid():
                inventory_serializer.save()
                return Response(inventory_serializer.data, status=status.HTTP_200_OK)
            return Response(inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        """
        Eliminación de un movimiento de un Inventario


        Eliminación lógica de un movimiento de un Inventario
        """
        inventory = self.get_queryset().filter(id=pk).first() # get instance        
        if inventory:
            inventory.state = False
            inventory.save()
            return Response({'message':'movimiento de un Inventario eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe el movimiento de un Inventario con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
