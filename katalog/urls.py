# TODO: Implement Routings Here
from django.contrib import admin
from django.urls import path, include
from katalog.views import katalog

urlpatterns = [
    path('', katalog, name='katalog'),
]