from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated'))

    class Meta:
        abstract = True
