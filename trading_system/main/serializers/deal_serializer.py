from rest_framework import serializers
from main.models import Deal


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ('product', 'cost', "volume","type")

    def create(self, validated_data):
        min_cost = float(validated_data.get("cost",-1))
        user = None
        request = self.context.get("request")
        if request and hasattr(request,"user"):
            user = request.user
        if user is None:
            error = {"message":"Неизвестный юзер"}
            raise serializers.ValidationError(error)
        if (min_cost/100)*validated_data.get("product").percent <= user.balance:
            deal = Deal.objects.create(status="Заявка",**validated_data)
            return deal
        else:
            error = {"message":"Недостаточно средств на балансе"}
            raise serializers.ValidationError(error)


class DealFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = "__all__"