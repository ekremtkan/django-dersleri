from django.contrib import admin
from django.urls import path
from .views import *
app_name="home"

urlpatterns = [
    path('index/',home_wiev ),
    path('',home_wiev ,name="homepg"),
]
