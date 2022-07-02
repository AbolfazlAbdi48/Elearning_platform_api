from dataclasses import field
from rest_framework import serializers
from courses.models import Subject


class SubjectListSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField(method_name='get_courses')

    def get_courses(self, obj):
        courses = [
            course.title for course in obj.courses.get_queryset().only('title')
        ]
        return courses

    class Meta:
        model = Subject
        fields = '__all__'
