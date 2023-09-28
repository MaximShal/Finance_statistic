from rest_framework import serializers
from .models import RevenueStatistic


class RevenueStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = "__all__"
