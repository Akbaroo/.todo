from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('user'))
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))
    start = models.DateTimeField(_('time start'), auto_now_add=True)
    finish = models.DateTimeField(_('time finish'), null=True, blank=True)
