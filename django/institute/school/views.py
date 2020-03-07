from django.shortcuts import render
from .models import School,Student
from rest_framework import viewsets
from .serializers import SchoolSerializer, StudentSerializer

# Create your views here.

class SchooldetailViewSet(viewsets.ModelViewSet):
    ''' return all the object of school model'''
    queryset = School.objects.all()
    serializer_class = SchoolSerializer




class StudentdetailViewSet(viewsets.ModelViewSet):
    ''' return all the object of student model'''

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    ''' return particular student details '''

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        i_d = self.kwargs['id']
        return qs.filter(id=i_d)
    
    def perform_create(self, serializer):
        serializer.save(id=self.request.id)

class StudentschoolViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(school=self.kwargs['school_pk'])


class SchoolViewSet(viewsets.ModelViewSet):
    ''' return particular school details '''

    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        i_d = self.kwargs['id']
        return qs.filter(id=i_d)
    
    def perform_create(self, serializer):
        serializer.save(id=self.request.id)

