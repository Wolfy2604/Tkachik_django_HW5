from django.contrib import admin

from measurement.models import Sensor, Measure


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ['sensor_id', 'temperature', 'date', 'photo']
