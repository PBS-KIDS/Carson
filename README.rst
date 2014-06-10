Introduction
------------
Carson helps you implement current best practices in responsive design,
allowing you to selectively resize or hide images to cater to varying screen
form factors. Carson will take care of loading an image over the network in
varying sizes automatically. It currently supports PNG and JPEG formats.

Installation
------------
``pip install bates``

``./manage.py syncdb``

``./manage.py collectstatic``

Admin
-----
This is where Image Profiles and Origins are created.

JavaScript
----------
Resized images are requested via "data-carson-size" attribute of <img> tags.
