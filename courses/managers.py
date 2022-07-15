from django.db import models


class CourseManager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def student_courses(self, user):
        return self.filter(students__in=[user])
