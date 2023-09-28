from collections import defaultdict
from django.db.models import Sum, Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import RevenueStatistic
from .serializers import RevenueStatisticSerializer


class RevenueStatisticViewSet(ModelViewSet):
    serializer_class = RevenueStatisticSerializer
    queryset = RevenueStatistic.objects.all()

    def analyze(self, request):
        result = defaultdict(list)
        grouped_queryset = RevenueStatistic.objects.values('date', 'name').annotate(
            total_revenue=Sum('revenue'),
            total_spend=Sum('spend__spend', distinct=True),
            total_impressions=Avg('spend__impressions', distinct=True),
            total_clicks=Sum('spend__clicks', distinct=True),
            total_conversion=Avg('spend__conversion', distinct=True)
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
