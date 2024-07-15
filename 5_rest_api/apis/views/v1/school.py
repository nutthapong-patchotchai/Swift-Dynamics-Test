from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import School, Classroom, Teacher, Student
from apis.serializers import SchoolSerializer, SchoolDetailSerializer, ClassroomSerializer, ClassroomDetailSerializer
from apis.filters import SchoolFilter, ClassroomFilter


class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter

class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['classrooms_count'] = instance.classrooms.count()
        data['teachers_count'] = Teacher.objects.filter(classrooms__school=instance).distinct().count()
        data['students_count'] = Student.objects.filter(classroom__school=instance).count()
        return Response(data)

class ClassroomListCreateView(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

class ClassroomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer