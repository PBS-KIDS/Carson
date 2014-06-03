from django.conf import settings
from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from bates.images.models import Mezzanine, ImageProfile


class MezzanineAdmin(AdminImageMixin, admin.ModelAdmin):
    list_filter = ['origin']
    list_display = ['__unicode__', 'origin', 'preview']

    exclude = ['origin']

    def queryset(self, request):
        images = super(MezzanineAdmin, self).queryset(request)
        return images.filter(origin__owner=request.user)

    def preview(self, instance):
        resized_image_url = '%s%s' % (settings.SITE_URL,
            instance.image_field.path.split(settings.MEDIA_ROOT)[1])
        return u'<img src="%s?size=small" />' % resized_image_url

    preview.allow_tags = True


class ImageProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'width', 'quality']

    exclude = ['owner']

    def queryset(self, request):
        image_profiles = super(ImageProfileAdmin, self).queryset(request)
        return image_profiles.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        form.instance.owner = request.user
        super(ImageProfileAdmin, self).save_model(request, obj, form, change)


admin.site.register(Mezzanine, MezzanineAdmin)
admin.site.register(ImageProfile, ImageProfileAdmin)
