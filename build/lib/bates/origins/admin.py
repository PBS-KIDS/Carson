from django.conf import settings
from django.contrib import admin

from bates.origins.models import Origin


class OriginAdmin(admin.ModelAdmin):
    list_display = ['namespace', 'base_url', 'preview']

    exclude = ['owner']

    def queryset(self, request):
        origins = super(OriginAdmin, self).queryset(request)
        return origins.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        form.instance.owner = request.user
        super(OriginAdmin, self).save_model(request, obj, form, change)

    def preview(self, instance):
        preview_markup = u''

        for image in instance.images.all()[:5]:
            resized_image_url = '%s%s' % (settings.SITE_URL,
                image.image_field.path.split(settings.MEDIA_ROOT)[1])
            image_markup = u'<img src="%s?size=small" />' % resized_image_url
            preview_markup = preview_markup + image_markup
        #TODO: Potential improvement: Pagination?
        if instance.images.count() > 5:
            preview_markup = preview_markup + '<p>(rest hidden)</p>'

        return preview_markup

    preview.allow_tags = True


admin.site.register(Origin, OriginAdmin)
