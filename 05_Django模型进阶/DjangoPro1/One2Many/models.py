from django.db import models

# 一对多关系
class UserType(models.Model):
    name = models.CharField(max_length=30)

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)

    # 外键
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)  # 级联删除
    # user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)  # 保护模式
    # user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=True)  # 置空模式
    # user_type = models.ForeignKey(UserType, on_delete=models.SET_DEFAULT, default=1)  # 置空模式
    # user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)  # NOTHING

    # on_delete参数主要有以下⼏个可选值：
    # models.CASCADE: 表示级联删除，即删除UserType时，相关联的UserInfo也会被删除。
    # models.PROTECT: 保护模式，阻⽌级联删除。
    # models.SET_NULL: 置空模式，设为null，null = True参数必须具备
    # models.SET_DEFAULT: 置默认值, 设为默认值，default参数必须具备
    # models.SET(): 删除的时候重新动态指向⼀个实体访问对应元素，可传函数
    # models.DO_NOTHING: 什么也不做。

    # related_name: 关联名称, 设置反向查找的名称, 原本使用user_set改为users
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT, related_name='users')



