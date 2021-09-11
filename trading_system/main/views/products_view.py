
from numpy.core.fromnumeric import sort
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from main.models import Product
import numpy as np

class ProductsView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        product_id = int(self.request.query_params.get('product',0))
        #sorted_by = self.request.query_params.get('sorted_by',0)
        descending = bool(self.request.query_params.get("descending",False))
        number = int(self.request.query_params.get("number",0))
        product = get_object_or_404(Product,pk=product_id)
        data = np.column_stack((
            product.dates,
            product.opening,
            product.max_data,
            product.min_data,
            product.closing,
            product.volume
        ))
        data = data.astype(np.int64)
        sorted_data = data[data[:,0].argsort()]
        if descending:
            sorted_data = sorted_data[::-1]
        if number > 0:
            sorted_data = sorted_data[:number]
        return Response({"data":sorted_data.tolist()})
