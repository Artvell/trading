from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from main.serializers import ProductSerializer
from main.models import Product

class ItemsView(ListAPIView):
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer