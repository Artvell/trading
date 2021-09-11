from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from main.models import Individual
from main.serializers import IndividualSerializer

class IndividualView(CreateAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = (IsAuthenticated, )

class IndividualUpdateView(UpdateAPIView):
    lookup_field = "user"
    lookup_url_kwarg = "pk"
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = (IsAuthenticated, )