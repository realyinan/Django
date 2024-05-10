from django.contrib import admin
from django.urls import path
from App.views import *

urlpatterns = [
    path('index/', index),
    path('admin/', admin.site.urls),
]
