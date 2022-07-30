from rest_framework import serializers
from courses.models import Chapter, Subject, Course


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
    subjects = serializers.SerializerMethodField(method_name='get_subjects')
    owner_name = serializers.CharField(source='owner.get_full_name')
    chapters_count = serializers.IntegerField(source='chapters.count')

    def get_subjects(self, obj):
        subjects = [
            {'title': subject.title, 'id': subject.id} for subject in obj.subject.get_queryset()
        ]
        return subjects

    class Meta:
        model = Course
        fields = ('id', 'owner_name', 'description', 'title',
                  'slug', 'subjects', 'price', 'chapters_count')


class CourseDetailSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField(method_name='get_subjects')
    chapters = serializers.SerializerMethodField(method_name='get_chapters')
    owner_name = serializers.CharField(source='owner.get_full_name')

    def get_subjects(self, obj):
        subjects = [
            {'title': subject.title, 'id': subject.id} for subject in obj.subject.get_queryset()
        ]
        return subjects

    def get_chapters(self, obj):
        chapters = [
            {
                "id": chapter.id,
                "title": chapter.title
            } for chapter in obj.chapters.get_queryset()
        ]
        return chapters

    class Meta:
        model = Course
        fields = (
            'id', 'owner_name', 'description', 'title', 'slug', 'subjects', 'price',
            'owner_name', 'chapters'
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('subject', 'title', 'description', 'price')


class ChapterDetailSerializer(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField(method_name='get_contents')

    def get_contents(self, obj):
        contents = [
            {"id": content.id, "title": content.title} for content in obj.contents.get_queryset()
        ]
        return contents

    class Meta:
        model = Chapter
        fields = ('id', 'title', 'description', 'contents')
