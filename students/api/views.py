from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from courses.api.serializers import CourseListDetailSerializer
from courses.models import Course, Order, OrderDetail
from students.api.serializers import OrderDetailSerializer


class StudentCoursesList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CourseListDetailSerializer

    def get_queryset(self):
        return Course.objects.student_courses(self.request.user)


class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.validated_data.get('course')
            try:
                order = Order.objects.get(owner=request.user, is_paid=False)
                order_detail = OrderDetail(
                    order=order,
                    price=course.price,
                    course=course
                )
                order_detail.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Order.DoesNotExist:
                order = Order(owner=request.user)
                order_detail = OrderDetail(
                    order=order,
                    price=course.price,
                    course=course
                )
                order.save()
                order_detail.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
