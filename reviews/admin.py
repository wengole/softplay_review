from django.contrib import admin
from .models import SoftPlayCentre


@admin.register(SoftPlayCentre)
class SoftPlayCentreAdmin(admin.ModelAdmin):
    pass
