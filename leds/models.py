from django.db import models
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Preset(models.Model):
    MODES = [
            ('RB', 'rainbow'),
            ('SO', 'solid_color'),
            ('CW', 'color_wipe'),
            ('MR', 'meteor_rain'),
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
    color = ColorField(default="#FF0000")
    
    def __str__(self):
        return self.preset_name


    @classmethod
    def get_all_modes(self):
        return self.MODES

