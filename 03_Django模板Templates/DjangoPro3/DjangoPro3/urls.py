from django.contrib import admin
from django.urls import path
from App.views import *

urlpatterns = [
    path('index/', index),
    path('block/', block),
    path('child/', child),

    path('admin/', admin.site.urls),
]
