from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('apply', views.start),
    path('apply2', views.apply),
    path('result', views.approve),
]