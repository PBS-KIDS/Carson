from StringIO import StringIO

from django.core.files import File
from django.http import HttpResponse

import requests
from requests.auth import HTTPBasicAuth

from bates.core.exceptions import HttpResponseException
from bates.images.models import Mezzanine


def get_or_create_mezzanine(origin, pathname):
    mezzanine_path = '%s/%s' % (origin.namespace, pathname)
    mezzanine_records = Mezzanine.objects.filter(origin=origin,
        image_field=mezzanine_path)

    if mezzanine_records:
        mezzanine = mezzanine_records.get()
    else:
        request_authentication = None
        if origin.username and origin.password:
            request_authentication = HTTPBasicAuth(origin.username,
                origin.password)

        request_url = '%s%s' % (origin.base_url, pathname)
        response = requests.get(request_url, auth=request_authentication)

        if response.status_code != 200:
            raise HttpResponseException(response.status_code, response.text)

        response_image = StringIO(response.content)

        mezzanine = Mezzanine()
        mezzanine.origin = origin
        mezzanine.image_field.save(pathname, File(response_image))
        mezzanine.save()

    return mezzanine


def inspect_image_url(pathname):
    pathname_without_querystring = pathname.split('?')[0]
    file_extension = pathname_without_querystring.split('.')[-1].lower()

    image_format = None
    image_mime_type = None

    if file_extension == 'png':
        image_format = 'PNG'
        image_mime_type = 'image/png'
    elif file_extension in ['jpg', 'jpeg']:
        image_format = 'JPEG'
        image_mime_type = 'image/jpeg'

    return (image_format, image_mime_type)
