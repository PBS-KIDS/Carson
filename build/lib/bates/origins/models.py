from django.contrib.auth.models import User
from django.db import models

from bates.core.models import TimeStamp


class Origin(TimeStamp):
    owner = models.ForeignKey(User, related_name='origins')
    namespace = models.SlugField(max_length=200, unique=True)

    base_url = models.URLField(max_length=500)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return u'%s' % self.namespace
