from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.model_form_upload, name='input_form'),
]