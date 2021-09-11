from rest_framework import serializers
from main.models import Product

class ProductSerializer(serializers.ModelSerializer):
    purchase = serializers.SerializerMethodField()
    sale = serializers.SerializerMethodField()
    percent = serializers.SerializerMethodField()

    def get_purchase(self, obj):
        return obj.opening[-1]

    def get_sale(self, obj):
            return obj.closing[-1]
    
    def get_percent(self, obj):
        purch = obj.opening[-1]
        sale = obj.closing[-1]
        return (sale-purch)/purch*100

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "purchase",
            "sale",
            "percent"
        )
