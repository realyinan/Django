from django.db import models

class userModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()  # 非负数

