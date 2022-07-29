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


class CourseListDetailSerializer(serializers.ModelSerializer):
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


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('subject', 'title', 'description', 'price')
