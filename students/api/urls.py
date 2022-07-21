from django.urls import path
from .views import (
    StudentCoursesList,
    OrderDetailView,
)

urlpatterns = [
    path('my-courses/', StudentCoursesList.as_view(), name='student-course-list'),
    path('order-detail/add', OrderDetailView.as_view(), name='order-detail'),
]
