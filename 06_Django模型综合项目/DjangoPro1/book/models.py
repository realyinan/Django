from django.db import models
from author.models import *
from publisher.models import *

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='书名')
    publish_date = models.DateField(verbose_name='出版时间')
    # 外键，book:author = N:1
    # on_delete=models.CASCADE: 级联删除
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='作者')
    # 多对多关系，book:publisher=N:N
    publishers = models.ManyToManyField(Publisher, verbose_name='出版社')

    def __str__(self):
        return self.title