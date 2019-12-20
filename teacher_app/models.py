from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=12) # 所有的字段类型都以什么什么Field结尾的
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)

    # 魔法函数，显示实例的时候，显示这个实例的name属性，Python的Console需要重新启动。如果改变了表结构，还需要迁移
    # def __str__(self):
    #     return self.name
    def __str__(self):
        return self.name


