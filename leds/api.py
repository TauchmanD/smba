from django.shortcuts import get_object_or_404

from ninja import Router

from .models import Preset
from .schema import PresetResponse


router = Router()

@router.get("/")
def index(request):
    return { 'status': 'running'}


@router.get("/preset", response=PresetResponse)
def get_active_preset(request):
    active_preset = Preset.objects.get(active=True)
    return active_preset


@router.get("/preset/{preset_id}", response=PresetResponse)
def get_preset(request, preset_id: int):
    preset = get_object_or_404(Preset, id=preset_id)
    return preset

@router.put("/preset/{preset_id}")
def set_active_preset(request, preset_id: int):
    new_preset = get_object_or_404(Preset, id=preset_id)
    active_preset = Preset.objects.get(active=True)
    active_preset.active = False
    active_preset.save()
    new_preset.active = True
    new_preset.save()
    return {"success": True}
    
