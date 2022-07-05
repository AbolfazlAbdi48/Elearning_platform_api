from rest_framework.generics import ListAPIView

from courses.models import Subject

from .serializers import SubjectListSerializer

# create your views here.

class SubjectList(ListAPIView):
    """
    get:
        return all subjects list.
    """

    serializer_class = SubjectListSerializer
    queryset = Subject.objects.all()
    