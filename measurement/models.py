from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True, blank=True)


class Measure(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measure')
    temperature = models.FloatField()
    date = models.DateField()
    photo = models.ImageField(null=True, blank=True)