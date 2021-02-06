from django.shortcuts import render

# Create your views here.
from student.models import Student

from django.views import View
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentModelSerializer


class Student1View(View):

    def get(self, request):
        data_dict = {"name": 'xiaowang', "age": 19}

        return JsonResponse(data_dict)


class Student2Api(APIView):
    def get(self, request):
        data_dict = {"name": 'xiaowang', "age": 19}

        return Response(data_dict)


class Student3Apiview(APIView):
    def get(self, request):
        student_list = Student.objects.all()
        print(student_list)

        serializer = StudentModelSerializer(instance=student_list, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self,request):
        # 接受post请求数据
        data_dict = request.data
        print(data_dict)
        #调用序列化器
        serializer = StudentModelSerializer(data=data_dict)
        #验证
        serializer.is_valid(raise_exception=True)
        # 反序列化，保存数据
        serializer.save()

        return Response(serializer.data)

