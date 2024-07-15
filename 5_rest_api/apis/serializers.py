# serializers.py
from rest_framework import serializers
from .models import School, Classroom, Teacher, Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolDetailSerializer(serializers.ModelSerializer):
    classrooms_count = serializers.IntegerField(read_only=True)
    teachers_count = serializers.IntegerField(read_only=True)
    students_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classrooms_count', 'teachers_count', 'students_count']

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField(many=True, read_only=True)
    students = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'school', 'teachers', 'students']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherDetailSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    classrooms = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'school', 'classrooms']

    def get_school(self, obj):
        # Assuming school is related through classrooms
        classrooms = obj.classrooms.all()  # Get all related classrooms
        schools = classrooms.values_list('school__name', flat=True)  # Extract school names
        return list(schools)  # Return as a list of school names

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    school  = serializers.StringRelatedField(source='classroom.school')
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender','school','classroom']
