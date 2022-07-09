from dataclasses import field
from rest_framework import serializers
from courses.models import Subject, Course


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


class CourseListSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField(method_name='get_chapters')
    subjects = serializers.SerializerMethodField(method_name='get_subjects')

    def get_chapters(self, obj):
        chapters = [
            chapter.title for chapter in obj.chapters.get_queryset().only('title')
        ]
        return chapters

    def get_subjects(self, obj):
        subjects = [
            subject.title for subject in obj.subject.get_queryset().only('title')
        ]
        return subjects

    class Meta:
        model = Course
        fields = ('owner', 'subjects', 'title', 'description', 'chapters')
