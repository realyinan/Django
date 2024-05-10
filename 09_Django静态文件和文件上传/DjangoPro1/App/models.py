from django.db import models

# 用户
class UserModel(models.Model):
    # 名字
    name = models.CharField(max_length=30, unique=True)
    # 头像路径
    icon = models.CharField(max_length=255)

# 相册
class PhotoModel(models.Model):
    # 图片链接
    # 图片所属用户
    img = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)