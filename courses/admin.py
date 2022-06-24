from django.contrib import admin
from .models import Subject, Course, Chapter, Content

# Register your models here.


class ChapterInline(admin.StackedInline):
    model = Chapter


class ContentInline(admin.StackedInline):
    model = Content


class SubjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'owner')
    inlines = [ChapterInline]


class ChapterAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'course')
    inlines = [ContentInline]


class ContentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'chapter')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Content, ContentAdmin)
