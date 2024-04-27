# BloodLevelApp/urls.py
from django.urls import path

# from BloodLevelApp.views import index
from BloodLevelApp import views


urlpatterns = [
    # path('', index),
    path('', views.index, name="index"),
    path('api/getBloodLevels/', views.get_blood_levels, name='get_blood_levels'),
]