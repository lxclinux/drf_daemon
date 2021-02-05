from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=32, verbose_name='名字')
    sex = models.BooleanField(default=1, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    class_null = models.CharField(max_length=5, verbose_name='班级')
    description = models.TextField(max_length=1000, verbose_name='备注')

    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name
