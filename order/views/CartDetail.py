from rest_framework import generics
from order.models import Cart
from order.serializers.Cart import CartSerializer
from rest_framework.views import APIView
# Create your views here.


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer