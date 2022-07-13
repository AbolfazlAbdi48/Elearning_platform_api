from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from .models import Course
from extensions.utils import slug_generator


@receiver(pre_save, sender=Course)
def save_course_slug(sender, instance, *args, **kwargs):
    if len(instance.slug) < 5:
        instance.slug = slugify(slug_generator(15))
