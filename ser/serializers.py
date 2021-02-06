from django.views import View
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    class_null = serializers.CharField()
    description = serializers.CharField()


'''
    在drf中对于客户端提供的数据，往往需要验证数据的有效性，这部分代码是写在序列化器中的
    在序列化器中，已经提供了三个地方给我们针对客户端提交的数据进行验证
    1. 内置选项，在字段声明的小圆括号中，已选项作为验证提交
    2. 自定义方法，在序列化器中作为对象方法来验证[这部分方法，必须以 'validate_<字段>'或者 'validate' 作为函数方法名]
    3. 自定义函数，在序列化器外，提前声明一个验证代码，然后在字段声明的小圆括号中，通过 "validators=[验证函数1， 验证函数2..]"
    
'''


class Student3Serializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=20)
    sex = serializers.BooleanField(required=True)
    age = serializers.IntegerField(min_value=0, max_value=150)
    class_null = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(max_length=1000, required=False)

    #验证单个字段
    def validate_name(self, data):
        if data == 'root':
            raise serializers.ValidationError('当前字段不能叫root')
        return data

    def validate_age(self, data):
        if data < 10:
            raise serializers.ValidationError('当前注册年龄必须10岁以上')
        return data

        # 验证多个字段

    def vilidate(self, data_dict):
        print(data_dict)

        name = data_dict.get("name")
        print(name)
        age = data_dict.get('age')

        if name == 'liuxingchen':
            raise serializers.ValidationError('当前name：liuxingchen已使用')
        return data_dict
