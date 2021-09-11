from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from main.serializers import NewsSerializer, NewsCategorySerializer, NewsPreviewSerializer
from main.models import News, NewsCategory

class NewsListView(ListAPIView):
    queryset = NewsCategory.objects.filter(news__isnull=False)
    serializer_class = NewsCategorySerializer
    permission_classes = (AllowAny,)

class NewsItemView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)

class NewsPreviewList(ListAPIView):
    queryset = News.objects.all().order_by("-date")[:6]
    serializer_class = NewsPreviewSerializer
    permission_classes = (AllowAny,)