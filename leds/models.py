from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Preset(models.Model):
    MODES = [
            ('RB', 'rainbow'),
            ('CB', 'centered_rainbow'),
            ('BR', 'breathing'),
            ('SO', 'solid_color'),
            ('PS', 'pulsing_stripes'),
    ]

    preset_name = models.CharField(
            default='New Preset',    
            max_length=30          
    )
    mode = models.CharField(
                default='SO',
                max_length=20,
                choices=MODES,
    )
    active = models.BooleanField(
                default=False
            )
    speed = models.PositiveIntegerField(
                default=50,
                validators=[
                    MaxValueValidator(100),
                    MinValueValidator(1),
                ]
    )
    led_settings = models.JSONField(
                default=dict(color="#ffffff")
            )
    
    def __str__(self):
        return self.preset_name


    @classmethod
    def get_all_modes(self):
        return self.MODES

