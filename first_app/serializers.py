from rest_framework import serializers
from .models import StudentModel, Course


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    # course = serializers.StringRelatedField(many=True)
    course = CourseSerializers(many=True)

    class Meta:
        model = StudentModel
        fields = '__all__'
