from rest_framework import generics
from rest_framework.response import Response
from apis.models import Teacher
from apis.serializers import TeacherSerializer, TeacherDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from apis.filters import TeacherFilter

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer