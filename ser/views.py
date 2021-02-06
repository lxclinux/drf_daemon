# from django.shortcuts import render, HttpResponse
import json

from django.http import HttpResponse

# Create your views here.
from django.views import View
from student.models import Student
from ser.serializers import StudentSerializer
from .serializers import Student3Serializer


class Student1View(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        print(student)
        serializers = StudentSerializer(instance=student)
        print(serializers.data)
        return HttpResponse('ok')


class Student2View(View):
    def get(self, request):
        student = Student.objects.all()
        serializers = StudentSerializer(instance=student, many=True)

        return HttpResponse(serializers.data)


class Student3View(View):
    def post(self, request):
        data_string = request.body.decode()
        # print(data)  # b'{\n    "name": "xiaowang",\n    "age": 23,\n    "class_null": 3,\n    "sex": 2\n\n\n}'
        data_json = json.loads(data_string)
        # print(data_json) # {'name': 'xiaowang', 'age': 23, 'class_null': 3, 'sex': 2}
        serializer = Student3Serializer(data=data_json)
        result = serializer.is_valid(raise_exception=True)
        # print(result)
        # print(serializer.validated_data)
        # 验证后的数据: OrderedDict([('name', 'xiaowang'), ('sex', True), ('age', 23), ('class_null', '3')])
        return HttpResponse('ok')
