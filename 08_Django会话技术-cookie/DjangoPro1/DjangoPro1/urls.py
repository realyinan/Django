from django.contrib import admin
from django.urls import path
from user.views import *

urlpatterns = [
    path('', index),
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('admin/', admin.site.urls),
]
