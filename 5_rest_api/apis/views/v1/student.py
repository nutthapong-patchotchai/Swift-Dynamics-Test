from rest_framework import generics
from rest_framework.response import Response
from apis.models import Student
from apis.serializers import StudentSerializer, StudentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apis.filters import StudentFilter

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer