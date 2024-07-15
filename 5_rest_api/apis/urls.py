from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1.school import SchoolListCreateView, SchoolDetailView, ClassroomListCreateView, ClassroomDetailView
from .views.v1.teacher import TeacherListCreateView, TeacherDetailView
from .views.v1.student import StudentListCreateView, StudentDetailView

router = DefaultRouter()

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls)),
    path('schools/', SchoolListCreateView.as_view(), name='school-list-create'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    path('classrooms/', ClassroomListCreateView.as_view(), name='classroom-list-create'),
    path('classrooms/<int:pk>/', ClassroomDetailView.as_view(), name='classroom-detail'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
