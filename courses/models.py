from django.db import models
from django.utils.translation import gettext_lazy as _
from courses.managers import CourseManager
from extensions.base_models import BaseModel
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Subject(BaseModel):
    """
    The Subject main model.
    """
    title = models.CharField(max_length=50, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = _('subject')
        verbose_name_plural = _('subjects')

    def __str__(self):
        return f"{self.title}"


class Course(BaseModel):
    """
    The Course main model,
    ManyToOne relationship with :model: `User`,
    ManyToMany relationship with :model: `Subject`,
    ManyToMany relationship with :model: `User`.
    """
    class PublishStatus(models.TextChoices):
        PUBLISHED = 'p', _('published')
        DRAFT = 'd', _('draft')

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='courses_created', verbose_name=_('owner')
    )
    subject = models.ManyToManyField(
        Subject, related_name='courses', verbose_name=_('subject'))
    title = models.CharField(max_length=50, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(verbose_name=_('description'))
    students = models.ManyToManyField(
        User, related_name='my_courses', verbose_name=_('students'))
    status = models.CharField(
        max_length=10, choices=PublishStatus.choices, default=PublishStatus.DRAFT, verbose_name=_('status')
    )
    price = models.IntegerField(default=0, verbose_name=_('price'))

    objects = CourseManager()

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')

    def __str__(self):
        return f"{self.title} - {self.owner}"


class Chapter(BaseModel):
    """
    The Chapter main model,
    ManyToOne relationship with :model: `Course`.
    """
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='chapters', verbose_name=_('course')
    )
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))

    class Meta:
        verbose_name = _('chapter')
        verbose_name_plural = _('chapters')

    def __str__(self):
        return f"{self.title} - {self.course}"


class Content(BaseModel):
    """
    The Content main model,
    """
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name='contents', verbose_name=_('chapter')
    )
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    video_file = models.FileField(
        upload_to='contents/videos/', verbose_name=_('video file')
    )
    attached_file = models.FileField(
        upload_to='contents/files/', null=True, blank=True, verbose_name=_('attached files')
    )
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    class Meta:
        verbose_name = _('content')
        verbose_name_plural = _('contents')

    def __str__(self):
        return f"{self.title}"


class Order(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders', verbose_name=_('Owner')
    )
    is_paid = models.BooleanField(default=False, verbose_name=_('Is Paid'))
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created'))
    payment_date = models.DateTimeField(
        null=True, blank=True, verbose_name=_('Payment Date'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"{self.id} - {self.owner}"


class OrderDetail(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='courses', verbose_name=_('Course')
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_details', verbose_name=_('Order')
    )
    price = models.IntegerField(verbose_name=_('Price'))

    class Meta:
        verbose_name = _('Order Detail')
        verbose_name_plural = _('Order Details')

    def __str__(self):
        return f"{self.order} | {self.course} | order : {self.order.id}"
