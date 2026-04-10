from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_register, name='student_register'),
    path('course/', views.course_register, name='course_register'),
    path('report/', views.course_report, name='course_report'),
]
