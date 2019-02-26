from django.contrib import admin
from django.urls import path, include
from .views import InputImageView, InputDetailView

urlpatterns = [
    path('', InputImageView.as_view(), name='input_form'),
    path(r'^/(?P<pk>\d+)/$', InputDetailView.as_view(), name='input_image'),
]