from django.contrib import admin
from django.urls import path
from App.views import *

urlpatterns = [
    # 分页
    path('pageinate2/<int:page>/', pageinate2, name='pageinate2'),
    path('pageinate/<int:page>/', pageinate, name='pageinate'),
    path('get/', get_person),  # 查询数据
    path('update/', update_person),  # 修改数据
    path('add/', add_person),  # 添加数据
    path('del/', del_person),  # 删除数据
    path('admin/', admin.site.urls),
]
