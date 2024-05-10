from django.db import models

# 模型 <==> 表结构
# 类属性 <==> 表字段
# 对象 <==> 表的一行记录

class UserModel(models.Model):
    name = models.CharField(max_length=30, unique=True)  # 对应SQL name varchar(30) unique
    age = models.IntegerField(default=18)  # age int default 18
    sex = models.CharField(max_length=10)  # sex varchar(20)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name, self.age, self.sex}'


# 用户名称 - name
# 用户年龄 - age
# 用户性别 - sex
# 是否删除 - is_deleted


# 注意:
#   数据迁移 models表结构一旦改变就需要重新数据迁移
#   迁移的概念: 就是将模型映射到数据库的过程
#   ⽣成迁移⽂件:  python manage.py makemigrations
#   执⾏迁移:  python manage.py migrate


