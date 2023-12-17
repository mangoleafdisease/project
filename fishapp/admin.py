from django.contrib import admin
from .models import Fish
from .forms import FishForm
# Register your models here.


class FishAdmin(admin.ModelAdmin):
    form = FishForm


admin.site.register(Fish, FishAdmin)
