from django.contrib import admin
from .models import Subject, Course, Chapter, Content

# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter)
admin.site.register(Content)
