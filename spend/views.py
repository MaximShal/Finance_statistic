from collections import defaultdict
from django.db.models import Sum, Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import SpendStatistic
from .serializers import SpendStatisticSerializer


class SpendStatisticViewSet(ModelViewSet):
    serializer_class = SpendStatisticSerializer
    queryset = SpendStatistic.objects.all()

    def analyze(self, request):
        result = defaultdict(list)
        grouped_queryset = SpendStatistic.objects.values('date', 'name').annotate(
            total_revenue=Sum('revenue__revenue'),
            total_spend=Sum('spend', distinct=True),
            total_impressions=Avg('impressions', distinct=True),
            total_clicks=Sum('clicks', distinct=True),
            total_conversion=Avg('conversion', distinct=True)
        )
        for item in grouped_queryset:
            result[str(item['date'])].append({
                'name': item['name'],
                'total_revenue': item['total_revenue'],
                'total_spend': item['total_spend'],
                'total_impressions': item['total_impressions'],
                'total_clicks': item['total_clicks'],
                'total_conversion': item['total_conversion'],
            })
        return Response(data=result, status=status.HTTP_200_OK)
