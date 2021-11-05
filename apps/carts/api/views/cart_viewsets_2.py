from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.carts.api.serializers.cart_serializers import CartSerializer
from apps.users.api.serializers import UserListSerializer
from apps.carts.models import Carts


class CartViewSet(viewsets.ModelViewSet):
    """
    Consulta o actualiza un Carrito


    Características de los Carritos
    """
    serializer_class = CartSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        """
        Retorna un listado de Carritos


        Presentación de los datos a retornar de un Carrito
        """
        cart_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(cart_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        Permite la Creación de un Carrito


        A continuación se describen los datos para crear un Carrito
        """
        print(f"create_view user ({self.request.user})")
        print(f"create_view data ({request.data})")
        #serializer = self.serializer_class(self.request.user, data=request.data)        
        serializer = self.serializer_class(data=request.data)        
        if serializer.is_valid():
            print(f"create_view serializer ({serializer})")
            print(f"create_view serializer.data ({serializer.data})")
            #cart = serializer.save()
            serializer.save()
            #print(f"create_view cart ({cart})")
            return Response({'cart':serializer.data, 'message': 'Carrito para el usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Actualización de atributos de un Carrito


        A continuación se describen los datos para modificar un Carrito
        """
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            cart_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if cart_serializer.is_valid():
                cart_serializer.save()
                return Response(cart_serializer.data, status=status.HTTP_200_OK)
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        """
        Finaliza un Carrito


        Eliminación lógica de un Carrito
        """
        cart = self.get_queryset().filter(id=pk).first() # get instance        
        if cart:
            cart.state = False
            cart.save()
            return Response({'message':'Carrito eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Carrito con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
