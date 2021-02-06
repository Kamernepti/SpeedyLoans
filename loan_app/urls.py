from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index),
    path('start', views.start),
    path('submit', views.apply),
    path('result', views.result),
    path('success', views.success), # create a view
    path('approved', views.approved),
    path('denied', views.denied), # create a view
] 