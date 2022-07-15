from django.urls import path
from .views import (
    StudentCoursesList,
)

urlpatterns = [
    path('my-courses/', StudentCoursesList.as_view(), name='student-course-list'),
]
