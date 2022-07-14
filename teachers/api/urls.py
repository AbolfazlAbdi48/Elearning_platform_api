from django.urls import path
from .views import (
    CourseCreate,
    CourseUpdate,
    ChapterListCreate,
    ContentListCreate
)

urlpatterns = [
    # courses
    path('courses/create/', CourseCreate.as_view(), name='course-create'),
    path('courses/update/<int:pk>/<slug:slug>', CourseUpdate.as_view(), name='course-update'),

    # chapters
    path('chapters/<int:course_pk>', ChapterListCreate.as_view(), name='chapter-list-create'),

    # contents
    path('contents/<int:chapter_pk>', ContentListCreate.as_view(), name='content-list-create'),
]
