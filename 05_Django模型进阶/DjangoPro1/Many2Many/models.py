from django.db import models

# 多对多
# 电影
class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(default=90)

# 用户
class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    # 多对多关系
    movies = models.ManyToManyField(Movie)
