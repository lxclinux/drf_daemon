from student.models import Student
from rest_framework import serializers


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, data_dict):
        name = data_dict.get("name")
        age = data_dict.get("age")

        return data_dict
