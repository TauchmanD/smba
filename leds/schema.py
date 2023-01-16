from ninja import Schema

class PresetResponse(Schema):
    id: int
    mode: str
    active: bool
    speed: int
    led_settings: dict

