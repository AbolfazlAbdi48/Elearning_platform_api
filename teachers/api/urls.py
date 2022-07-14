from django.urls import path
from .views import (
    CourseCreate,
    CourseUpdate
)

urlpatterns = [
    # courses
    path('courses/create/', CourseCreate.as_view(), name='course-create'),
    path('courses/update/<int:pk>/<slug:slug>', CourseUpdate.as_view(), name='course-update'),
]
