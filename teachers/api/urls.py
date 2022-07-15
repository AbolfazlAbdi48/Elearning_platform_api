from django.urls import path
from .views import (
    ChapterDelete,
    ChapterUpdate,
    ContentDetail,
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
    path('chapters/update/<int:pk>', ChapterUpdate.as_view(), name='chapter-update'),
    path('chapters/delete/<int:pk>', ChapterDelete.as_view(), name='chapter-delete'),

    # contents
    path('contents/<int:chapter_pk>', ContentListCreate.as_view(), name='content-list-create'),
    path('contents/detail/<int:pk>', ContentDetail.as_view(), name='content-detail-update-delete'),
]
