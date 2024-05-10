from django.db import models

# 用户
class UserModel(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    age = models.IntegerField(default=18)

