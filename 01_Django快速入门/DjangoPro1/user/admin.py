from django.contrib import admin
from user.models import *

# 后台管理系统的使用
#   1. 在这里注册对应的模型
#   2. 创建超级管理员账号和密码: python manage.py createsuperuser
#   3. 根路由urls.py添加: path('admin/', admin.site.urls)
admin.site.register(UserModel)


