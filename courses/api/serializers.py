from rest_framework import serializers
from courses.models import Subject, Course


class SubjectListSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField(method_name='get_courses')

    def get_courses(self, obj):
        courses = [
            {'title': course.title, 'slug': course.slug} for course in obj.courses.get_queryset()
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
            chapter.title for chapter in obj.chapters.get_queryset()
        ]
        return chapters

    def get_subjects(self, obj):
        subjects = [
            {'title': subject.title, 'slug': subject.slug} for subject in obj.subject.get_queryset()
        ]
        return subjects

    class Meta:
        model = Course
        fields = ('owner', 'description', 'title', 'chapters', 'subjects')
