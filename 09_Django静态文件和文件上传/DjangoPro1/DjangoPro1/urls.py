from django.contrib import admin
from django.urls import path
from App.views import *

urlpatterns = [
    # 静态文件
    path('index/', index, name='index'),
    path('index2/', index2, name='index2'),

    # 上传文件
    path('upload1/', upload1, name='upload1'),
    path('upload2/', upload2, name='upload2'),

    path('showicon/', show_icon, name='showicon'),

    path('admin/', admin.site.urls),
]
