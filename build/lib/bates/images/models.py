from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from sorl.thumbnail import ImageField

from bates.core.models import NameAndDescription, TimeStamp
from bates.origins.models import Origin


def image_location(instance, filename):
    return '%s/%s' % (instance.origin.namespace, filename)

class Mezzanine(TimeStamp):
    origin = models.ForeignKey(Origin, related_name='images')
    image_field = ImageField(upload_to=image_location)

    def __unicode__(self):
        image_url = self.image_field.path.split(settings.MEDIA_ROOT)[1]
        return u'%s' % image_url


class ImageProfile(NameAndDescription, TimeStamp):
    owner = models.ForeignKey(User, related_name='image_profiles')

    width = models.PositiveSmallIntegerField(null=False)
    quality = models.PositiveSmallIntegerField(null=False, default=100)

    class Meta:
        unique_together = ('owner', 'name')
