from django.contrib import admin
from django.urls import path, include
from katalog.views import katalog
from mywatchlist.views import show_html, show_json, show_xml

urlpatterns = [
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('', show_html, name='show_html')
]