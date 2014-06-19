Introduction
------------
Carson helps you implement current best practices in responsive design,
allowing you to selectively resize or hide images to cater to varying screen
form factors. Carson will take care of loading an image over the network in
varying sizes automatically. It currently supports PNG and JPEG formats.

Prerequisite
------------
- Memcache

Installation
------------
``pip install bates``

settings.py

#. Define memcache configuration (see https://docs.djangoproject.com/en/dev/topics/cache/#memcached).
#. Add the following to INSTALLED_APPS

#. 'bates.core'
#. 'bates.images'
#. 'bates.origins'

``./manage.py syncdb``

``./manage.py collectstatic``

Admin
-----
This is where Image Profiles and Origins are created.

TODO: Usage instructions and examples.

JavaScript
----------
Resized images are requested via "data-carson-size" attribute of <img>
tags.

TODO: Usage instructions and examples.
