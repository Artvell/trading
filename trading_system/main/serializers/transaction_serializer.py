from django.db.models import fields
from rest_framework import serializers
from main.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"