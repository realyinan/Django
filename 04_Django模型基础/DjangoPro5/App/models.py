from django.db import models

# 模型当中的字段类型和约束
class UserModel(models.Model):
    # uid会成为主键, 原来的id不会创建
    uid = models.AutoField(auto_created=True, primary_key=True)
    # CharField: 字符串类型, 唯一的, 索引
    name = models.CharField(max_length=30, unique=True, db_index=True)
    # InterGerField: 整数类型, default默认值
    age = models.IntegerField(default=18)
    # BooleanField: 布尔类型
    sex = models.BooleanField(default=True)
    # TextField: 大文本, 长字符串, null=True 表示可以为空, blank=True 表示在admin管理页面可以为空
    infor = models.TextField(null=True, blank=True)
    # FloatField: 浮点型
    salary = models.FloatField(default=10000.0)
    # DecimalField: 十进制小数, max_digits 表示最大长度 decimal_places 表示小数点后的位数
    money = models.DecimalField(max_digits=4, decimal_places=2, default=10.34)
    # 日期
    birthday = models.DateField(default='2005-03-04')
    birthday2 = models.DateTimeField(auto_now=True)  # 每一次修改后都会自动修改该时间为最新
    birthday3 = models.DateTimeField(auto_now_add=True)  # 第一次添加数据的时候的时间, 以后不会再修改

    # 文件和图片
    icon = models.FileField(null=True, blank=True, upload_to='static/uploads')
    icon2 = models.ImageField(null=True, blank=True,  upload_to='static/uploads')

    # 其他约束
    choices = (
        (1, '青铜'),
        (2, '白银'),
        (3, '黄金')
    )
    user_type = models.IntegerField(choices=choices, default=1,
                                    name='utype', verbose_name='用户类型')
    user_type2 = models.IntegerField(default=1, editable=False, db_column='utype2', verbose_name='用户类型2')

# 增删改查
class PersonModel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    age = models.IntegerField(default=18)

    class Meta:
        db_table = 'tb_person'

    def __str__(self):
        return f'{self.id}-{self.name}-{self.age}'

    def __repr__(self):
        return f'{self.id}-{self.name}-{self.age}'

# ORM 对象关系映射
# 模型类 => 表结构
# 类属性 => 表字段
# 一个对象 => 表中的一条记录
