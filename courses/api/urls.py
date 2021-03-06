from django.urls import path
from .views import (
    SubjectList,
    CourseList,
    CourseDetail
)

urlpatterns = [
    # subjects
    path('subjects/', SubjectList.as_view(), name='subject-list'),

    # courses
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>', CourseDetail.as_view(), name='course-detail'),
]