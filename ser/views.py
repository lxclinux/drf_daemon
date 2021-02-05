# from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
from django.views import View
from student.models import Student
from ser.serializers import StudentSerializer


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
        serializers = StudentSerializer(instance=student,many=True)

        return HttpResponse(serializers.data)