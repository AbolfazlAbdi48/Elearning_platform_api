from django.urls import path
from .views import (
    SubjectList
)

urlpatterns = [
    # subjects
    path('subjects/', SubjectList.as_view(), name='subject-list')
]