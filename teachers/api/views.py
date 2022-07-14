from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView
)
from courses.api.serializers import CourseSerializer
from courses.models import Chapter, Course
from courses.permissions import IsSuperUserOrOwner, IsSuperUserOrTeacher
from teachers.api.serializers import ChapterSerializer


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


class ChapterListCreate(ListCreateAPIView):
    permission_classes = [IsSuperUserOrTeacher, ]
    serializer_class = ChapterSerializer

    def get_queryset(self):
        return Chapter.objects.filter(
            course__pk=self.kwargs.get('course_pk'),
            course__owner__in=[self.request.user],
            course__status=Course.PublishStatus.PUBLISHED
        )

    def perform_create(self, serializer):
        return serializer.save(
            course_id=self.kwargs.get('course_pk')
        )
