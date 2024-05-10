# 子路由
from django.urls import path
from user.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('index2/', index2, name='index2'),
    path('users/', get_users, name='users')
]