from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
from main.serializers import DealSerializer, DealFullSerializer
from main.models import Deal

class DealCreateView(CreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = (IsAuthenticated, )


class DealListView(ListAPIView):
    serializer_class = DealFullSerializer
    permission_classes = (IsAuthenticated, )
    statuses = {
        "0":"Заявка",
        "1":"Ожидает оплаты",
        "3":"Оплачена",
        "4":"Исполнена",
        "5":"Аннулирована",
        "6":"Блокирована"
    }
    def get_queryset(self):
        queryset = Deal.objects.all(user_id=self.request.user)
        status = self.request.query_params.get('status')
        order_field = self.request.query_params.get('order_field')
        descending = bool(self.request.query_params.get('descending',False))
        if status is not None and status.isdigit() and (int(status)>-1 and int(status)<7):
            queryset = queryset.filter(status=self.statuses[status])
        if order_field is not None:
            queryset = queryset.order_by(order_field)
        if descending:
            queryset = queryset.reverse()
        return queryset