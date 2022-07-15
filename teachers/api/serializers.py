from rest_framework import serializers

from courses.models import Chapter, Content


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'description')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'title', 'description', 'video_file', 'attached_file', 'is_active')
