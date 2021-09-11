from rest_framework import serializers
from main.models import News



class NewsShortSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    def get_text(self, obj):
        return obj.text[:100]

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "text",
            "photo"
        )

class NewsPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "date"
        )

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"