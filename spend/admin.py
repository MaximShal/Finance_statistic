from django.contrib import admin
from .models import SpendStatistic


@admin.register(SpendStatistic)
class SpendStatisticAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'spend', 'impressions', 'clicks', 'conversion')
