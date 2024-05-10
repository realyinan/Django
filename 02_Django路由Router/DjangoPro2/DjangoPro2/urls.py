from django.contrib import admin
from django.urls import path, include
from App.views import *

urlpatterns = [

    # 1. 直接使用根路由
    # path('user/', index),

    # 2. 使用子路由: 使用include
    # path('user/', include('App.urls')),

    # 3.使用子路由: 使用include, 命名空间 namespace
    path('user/', include(('App.urls', 'App'), namespace='App')),

    path('admin/', admin.site.urls),
]
