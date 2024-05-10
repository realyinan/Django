from django.contrib import admin
from django.urls import path, include
from user.views import *

urlpatterns = [
    # 路由 url
    # 直接访问视图函数, 没有使用子路由
    # path('index/', index),
    # path('index2/', index2),

    # 使用子路由
    #   一个应用对应一个子路由
    path('user/', include('user.urls')),

    path('admin/', admin.site.urls),
]
