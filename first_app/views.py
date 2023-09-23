from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentModel
from .serializers import StudentSerializers

# Create your views here.


class StudentView(APIView):
    def get(self, request):
        data = StudentModel.objects.all()
        serializers = StudentSerializers(data, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailsView(APIView):
    def get(self, request, pk):
        student_data = StudentModel.objects.get(pk=pk)
        serializers = StudentSerializers(student_data)
        return Response(serializers.data)

    def put(self, request, pk):
        student_data = StudentModel.objects.get(pk=pk)
        serializers = StudentSerializers(student_data, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resuest, pk):
        student_data = StudentModel.objects.get(pk=pk)
        student_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
