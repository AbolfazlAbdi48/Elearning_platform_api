from django.urls import path
from .views import (
    CourseCreate,
    CourseUpdate,
    ChapterListCreate,
    ChapterDetail,
    ContentListCreate,
    ContentDetail,
)

urlpatterns = [
    # courses
    path('courses/create/', CourseCreate.as_view(), name='course-create'),
    path('courses/update/<int:pk>/<slug:slug>', CourseUpdate.as_view(), name='course-update'),

    # chapters
    path('chapters/<int:course_pk>', ChapterListCreate.as_view(), name='chapter-list-create'),
    path('chapters/detail/<int:pk>', ChapterDetail.as_view(), name='chapter-detail-update-delete'),

    # contents
    path('contents/<int:chapter_pk>', ContentListCreate.as_view(), name='content-list-create'),
    path('contents/detail/<int:pk>', ContentDetail.as_view(), name='content-detail-update-delete'),
]
