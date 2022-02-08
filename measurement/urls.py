from django.urls import path
from measurement.views import SensorsView, SensorDetailView, MeasureView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasureView.as_view()),
]
