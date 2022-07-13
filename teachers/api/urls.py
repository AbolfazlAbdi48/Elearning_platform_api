from django.urls import path
from .views import (
    CourseCreate
)

urlpatterns = [
    # courses
    path('courses/create/', CourseCreate.as_view(), name='course-create'),
]