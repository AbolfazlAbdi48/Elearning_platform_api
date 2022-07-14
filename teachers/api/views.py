from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from courses.api.serializers import CourseSerializer
from courses.models import Course
from courses.permissions import IsSuperUserOrOwner, IsSuperUserOrTeacher


class CourseCreate(CreateAPIView):
    permission_classes = [IsSuperUserOrTeacher, ]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        return serializer.save(
            owner=self.request.user,
            status=Course.PublishStatus.DRAFT
        )


class CourseUpdate(RetrieveUpdateAPIView):
    permission_classes = [IsSuperUserOrOwner, ]
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(status=Course.PublishStatus.PUBLISHED)
