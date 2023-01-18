from django.contrib import admin

# Register your models here.
from .models import Preset


class PresetAdmin(admin.ModelAdmin):
    list_display = ("id", "active", "preset_name", "mode", "color")
    exclude = ('active',)


admin.site.register(Preset, PresetAdmin)
