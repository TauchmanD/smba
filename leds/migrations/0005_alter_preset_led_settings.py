# Generated by Django 4.1.5 on 2023-01-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leds', '0004_preset_preset_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preset',
            name='led_settings',
            field=models.JSONField(default={'color': '#ffffff'}),
        ),
    ]