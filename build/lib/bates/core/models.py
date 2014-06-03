from django.db import models


class NameAndDescription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True	

    def __unicode__(self):
        return u'%s' % self.name


class TimeStamp(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
          abstract = True
