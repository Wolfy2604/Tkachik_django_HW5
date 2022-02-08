from rest_framework import serializers
from measurement.models import Sensor, Measure


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['sensor_id', 'temperature', 'date', 'photo']


class SensorDetailSerializer(serializers.ModelSerializer):
    measure = MeasureSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measure']


