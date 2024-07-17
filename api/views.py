from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
@api_view(['GET'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def student_detail(request, pk):
    if id is not None:
        try:
            stu = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            context = {'error': 'Student not found'}
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(stu)
        return Response(serializer.data)
    
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def student_update(request, pk):
    try:
        stu = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        context = {'error': 'Student not found'}
        return Response(context, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(instance=stu, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, pk):
    try:
        stu = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        context = {'error': 'Student not found'}
        return Response(context, status=status.HTTP_404_NOT_FOUND)
    
    stu.delete()
    return Response('Student deleted successfully')

