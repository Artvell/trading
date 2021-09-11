from django.http import request
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from main.serializers import TransactionSerializer
from main.models import Transaction

class TransactionListView(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user)
        order_field = self.request.query_params.get('order_field')
        descending = bool(self.request.query_params.get('descending',False))
        if order_field is not None:
            queryset = queryset.order_by(order_field)
        if descending:
            queryset = queryset.reverse()
        return queryset