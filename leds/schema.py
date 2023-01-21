from ninja import Schema

class PresetResponse(Schema):
    id: int
    preset_name: str
    mode: str
    active: bool
    color: str

