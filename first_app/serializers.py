from rest_framework import serializers
from .models import StudentModel, Course


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    # course = serializers.StringRelatedField(many=True)
    # course = serializers.PrimaryKeyRelatedField(many=True)
    # course = CourseSerializers(many=True)
    course = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='course_details'
    )

    class Meta:
        model = StudentModel
        fields = '__all__'
