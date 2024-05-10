from django.db import models

# 身份证
class IDCard(models.Model):
    idcard_num = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=200)

# 用户表
class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField(default=18)
    sex = models.BooleanField(default=False)
    # 一对一关系
    idcard = models.OneToOneField(IDCard, on_delete=models.PROTECT)


