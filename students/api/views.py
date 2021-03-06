from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from courses.api.serializers import CourseListSerializer
from courses.models import Course, Order, OrderDetail
from students.api.serializers import OrderSerializer, OrderDetailSerializer


class StudentCoursesList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CourseListSerializer

    def get_queryset(self):
        return Course.objects.student_courses(self.request.user)


class StudentOrderList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user).order_by('-created')


class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, format=None):
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.validated_data.get('course')
            try:
                order = Order.objects.get(owner=request.user, is_paid=False)
            except Order.DoesNotExist:
                order = Order(owner=request.user)
                order.save()

            if not (course.id,) in order.order_details.values_list('course'):
                order_detail = OrderDetail(
                    order=order,
                    price=course.price,
                    course=course
                )
                order_detail.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'course exist'}, status=status.HTTP_302_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = OrderDetailSerializer

    def get_object(self):
        return get_object_or_404(
            OrderDetail, order__is_paid=False, order__owner=self.request.user, pk=self.kwargs.get('pk')
        )
