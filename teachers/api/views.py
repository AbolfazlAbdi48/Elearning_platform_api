from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from courses.api.serializers import CourseSerializer
from courses.models import Chapter, Content, Course
from courses.permissions import (
    IsSuperUserOrOwner,
    IsSuperUserOrTeacher,
    ChapterAccess,
    ContentAccess
)
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
        qs = get_object_or_404(
            Course,
            pk=self.kwargs.get('course_pk'),
            status=Course.PublishStatus.PUBLISHED,
            owner=self.request.user
        )
        return qs.chapters.all()

    def perform_create(self, serializer):
        return serializer.save(
            course_id=self.kwargs.get('course_pk')
        )


class ChapterDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [ChapterAccess, ]
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ContentListCreate(ListCreateAPIView):
    permission_classes = [IsSuperUserOrTeacher, ]
    serializer_class = ContentSerializer

    def get_queryset(self):
        qs = get_object_or_404(
            Chapter,
            pk=self.kwargs.get('chapter_pk'),
            course__owner=self.request.user
        )
        return qs.contents.all()

    def perform_create(self, serializer):
        return serializer.save(
            chapter_id=self.kwargs.get('chapter_pk')
        )


class ContentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [ContentAccess, ]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
