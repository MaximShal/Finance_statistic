from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import SpendStatistic
from revenue.models import RevenueStatistic


class SpendStatisticViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.spends = []
        self.revenues = []
        for number in [5000.00, 10000.00]:
            spend = SpendStatistic.objects.create(
                name="car", date="2023-09-28", spend=number, impressions=5, clicks=11, conversion=2)
            revenue = RevenueStatistic.objects.create(
                name="car", spend_id=spend.id, date="2023-09-28", revenue=number+500)
            self.spends.append(spend)
            self.revenues.append(revenue)

    def test_analyze(self):
        response = self.client.get(reverse("spend-analyze"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["2023-09-28"][0]['total_revenue'], sum(revenue.revenue for revenue in self.revenues))
        self.assertEqual(response.data["2023-09-28"][0]['total_spend'], sum(spend.spend for spend in self.spends))
