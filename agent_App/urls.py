from django.urls import path
from . import views

urlpatterns = [
    path('user-agent/', views.index, name='index'),
    path('user-agent/info', views.device_info, name='info')
]