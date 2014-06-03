from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseBadRequest

from sorl.thumbnail import get_thumbnail

from bates.core.exceptions import HttpResponseException
from bates.images.models import Mezzanine, ImageProfile
from bates.images.utils import get_or_create_mezzanine, inspect_image_url
from bates.origins.models import Origin


def serve(request, namespace, pathname):
    try:
        origin = Origin.objects.get(namespace=namespace)
    except Origin.DoesNotExist:
        return HttpResponseNotFound('Invalid namespace %s' % namespace)

    image_format, image_mime_type = inspect_image_url(pathname)
    if image_format is None:
        return HttpResponseBadRequest('Only .png and .jpeg/.jpg are supported')

    try:
        mezzanine = get_or_create_mezzanine(origin, pathname)
    except HttpResponseException as response:
        return HttpResponse(response.message, status=response.status_code)

    image_size = request.GET.get('size', None)

    # Serve mezzanine image
    if image_size is None:
        return HttpResponse(mezzanine.image_field.file.read(), image_mime_type)

    # Serve resized image
    try:
        image_profile = ImageProfile.objects.get(owner=origin.owner,
            name=image_size)
    except ImageProfile.DoesNotExist:
        return HttpResponseNotFound('Invalid image profile %s' % image_size)

    # TODO: Width clamping so that it doesn't go over mezzanine size
    image = get_thumbnail(
        mezzanine.image_field,
        '%s' % image_profile.width,
        quality=image_profile.quality,
        format=image_format,
    )

    return HttpResponse(image.read(), mimetype=image_mime_type)
