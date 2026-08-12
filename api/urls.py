from django.urls import path
from .views import *
urlpatterns = [

    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),

    path('faculty/', FacultyListCreateView.as_view()),
    path('faculty/<int:pk>/', FacultyDetailView.as_view()),

    path('courses/', CourseListCreateView.as_view()),
    path('courses/<int:pk>/', CourseDetailView.as_view()),

    path('batches/', BatchListCreateView.as_view()),
    path('batches/<int:pk>/', BatchDetailView.as_view()),

    path('attendance/', AttendanceListCreateView.as_view()),
    path('attendance/<int:pk>/', AttendanceDetailView.as_view()),

    path('fees/', FeeListCreateView.as_view()),
    path('fees/<int:pk>/', FeeDetailView.as_view()),

    path('study-material/', StudyMaterialListCreateView.as_view()),
    path('study-material/<int:pk>/', StudyMaterialDetailView.as_view()),

    path('assignments/', AssignmentListCreateView.as_view()),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view()),

    path('contact-query/', ContactQueryListCreateView.as_view()),
    path('contact-query/<int:pk>/', ContactQueryDetailView.as_view()),
]