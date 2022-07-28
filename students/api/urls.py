from django.urls import path
from .views import (
    StudentCoursesList,
    StudentOrderList,
    OrderDetailView,
    OrderDetailDeleteView
)

urlpatterns = [
    path('my-courses/', StudentCoursesList.as_view(), name='student-course-list'),
    path('orders/', StudentOrderList.as_view(), name='order-list'),
    path('order-detail/add', OrderDetailView.as_view(), name='order-detail-add'),
    path('order-detail/delete/<int:pk>', OrderDetailDeleteView.as_view(), name='order-detail-delete'),
]
