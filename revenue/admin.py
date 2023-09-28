from django.contrib import admin
from .models import RevenueStatistic


@admin.register(RevenueStatistic)
class RevenueStatisticAdmin(admin.ModelAdmin):
    list_display = ('name', 'spend', 'date', 'revenue')
