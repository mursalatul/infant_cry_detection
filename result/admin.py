from django.contrib import admin

# Register your models here.

from result.models import TrustCounter

@admin.register(TrustCounter)
class TrustCounterAdmin(admin.ModelAdmin):
    list_display = ('count_number',)
