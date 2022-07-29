from rest_framework.generics import ListAPIView, RetrieveAPIView

from courses.models import Course, Subject

from .serializers import CourseListSerializer, SubjectListSerializer, CourseDetailSerializer

# create your views here.


class SubjectList(ListAPIView):
    """
    get:
        return all subjects list.
    """

    serializer_class = SubjectListSerializer
    queryset = Subject.objects.all()


class CourseList(ListAPIView):
    """
    get:
        return published courses for all users.
    """

    serializer_class = CourseListSerializer
    queryset = Course.objects.published()


class CourseDetail(RetrieveAPIView):
    """
    get:
        return published course by pk, slug.
    """
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.filter(status=Course.PublishStatus.PUBLISHED)