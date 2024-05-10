from django.contrib import admin
from django.urls import path
from App.views import *
urlpatterns = [
    path('request/', my_request),
    path('response/', my_response),
    path('admin/', admin.site.urls),
]
