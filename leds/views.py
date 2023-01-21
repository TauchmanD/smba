from django.shortcuts import render

from .models import Preset
# Create your views here.


def index(request):
    p = Preset.objects.order_by("-active")
    context = {'presets': p} 
    return render(request, 'leds/index.html', context)
