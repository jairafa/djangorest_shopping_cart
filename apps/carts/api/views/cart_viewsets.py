from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.carts.api.serializers.cart_serializers import CartSerializer
from apps.users.api.serializers import UserListSerializer
from apps.carts.models import Carts

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self, pk=None):
        #print(f"CartViewSet Ingresa al get_queryset pk ({pk})")
        if pk is None:
            carts = self.get_serializer().Meta.model.objects.filter(state=True)
            #for cart in carts:
            #    print(f"CartViewSet cart {cart}")
            return carts
        return self.get_serializer().Meta.model.objects.filter(user_id=pk, state=True).first()

    def list(self, request):
        cart_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(cart_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)   
        request.data['user'] = request.user.id     
        if serializer.is_valid():
            serializer.save()
            return Response({'cart':serializer.data, 'message': 'Carrito para el usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        request.data['user'] = request.user.id
        if self.get_queryset(request.user.id):
            # send information to serializer referencing the instance
            serializer = self.serializer_class(self.get_queryset(request.user.id), data=request.data)            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
