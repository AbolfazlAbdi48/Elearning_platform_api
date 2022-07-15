from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from courses.api.serializers import CourseListDetailSerializer
from courses.models import Course


class StudentCoursesList(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CourseListDetailSerializer

    def get_queryset(self):
        return Course.objects.student_courses(self.request.user)
