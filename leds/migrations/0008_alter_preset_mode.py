# Generated by Django 4.1.5 on 2023-01-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leds', '0007_remove_preset_led_settings_remove_preset_speed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preset',
            name='mode',
            field=models.CharField(choices=[('RB', 'rainbow'), ('SO', 'solid_color'), ('CW', 'color_wipe'), ('MR', 'meteor_rain')], default='SO', max_length=20),
        ),
    ]
