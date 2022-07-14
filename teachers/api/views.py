from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from courses.api.serializers import CourseSerializer
from courses.models import Chapter, Content, Course
from courses.permissions import IsSuperUserOrOwner, IsSuperUserOrTeacher
from teachers.api.serializers import ChapterSerializer, ContentSerializer


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
            course__owner__in=[self.request.user]
        )

    def perform_create(self, serializer):
        return serializer.save(
            course_id=self.kwargs.get('course_pk')
        )


class ChapterUpdate(RetrieveUpdateAPIView):
    permission_classes = [IsSuperUserOrTeacher]
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ChapterDelete(DestroyAPIView):
    permission_classes = [IsSuperUserOrTeacher,]
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ContentListCreate(ListCreateAPIView):
    permission_classes = [IsSuperUserOrTeacher, ]
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.filter(
            chapter__pk=self.kwargs.get('chapter_pk'),
            chapter__course__owner__in=[self.request.user]
        )

    def perform_create(self, serializer):
        return serializer.save(
            chapter_id=self.kwargs.get('chapter_pk')
        )
