# BloodLevelApp/urls.py
from django.urls import path

from BloodLevelApp.views import index


urlpatterns = [
    path('', index),
]