from rest_framework import serializers
from main.models import NewsCategory
from main.serializers import NewsShortSerializer

class NewsCategorySerializer(serializers.ModelSerializer):
    news = NewsShortSerializer(many=True, read_only=True)
    class Meta:
        model = NewsCategory
        fields = "__all__"