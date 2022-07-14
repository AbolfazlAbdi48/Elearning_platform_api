from rest_framework import serializers

from courses.models import Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('title', 'description')
