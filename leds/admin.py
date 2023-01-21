from django.contrib import admin

# Register your models here.
from .models import Preset


class PresetAdmin(admin.ModelAdmin):
    list_display = ("preset_name", "id", "active", "mode", "color")
    exclude = ('active',)


admin.site.register(Preset, PresetAdmin)
