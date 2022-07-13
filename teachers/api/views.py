from rest_framework.generics import CreateAPIView
from courses.api.serializers import CourseSerializer
from courses.models import Course
from courses.permissions import IsSuperUserOrTeacher


class CourseCreate(CreateAPIView):
    permission_classes = [IsSuperUserOrTeacher, ]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        return serializer.save(
            owner=self.request.user,
            status=Course.PublishStatus.DRAFT
        )
