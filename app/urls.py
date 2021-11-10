from django.urls import path
from app.views import ConvTemp, Conv,ConvTime



urlpatterns = [
    path('',Conv),
    path('temp/',ConvTemp,name='temp'),
    path('time/',ConvTime,name='time')
]
