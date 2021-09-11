from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from main.models import Entity
from main.serializers import EntitySerializer

class EntityView(CreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticated, )

class EntityUpdateView(UpdateAPIView):
    lookup_field = "user"
    lookup_url_kwarg = "pk"
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (IsAuthenticated, )