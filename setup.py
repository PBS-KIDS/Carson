import os
from setuptools import setup, find_packages

setup(
    name = "bates",
    version = "0.0.1",
    author = "PBS Kids Digital team",
    author_email = "kidstech@pbs.org",
    description = ("HTML5 adaptive images polyfill: a Django and javascript solution"),
    license = "MIT",
    keywords = "django python",
    url = "https://github.com/PBS-KIDS/Carson/",
    packages=find_packages(exclude=('tests',)), 
    install_requires=[
        'python-memcached>=1.53',
        'django>=1.5.4',
        'sorl-thumbnail==11.12',
        'requests==1.2.3'
    ],
    include_package_data=True,
    zip_safe=False, # Include static files (carson.js)
    long_description="Carson helps you implement current best practices in responsive design, allowing you to selectively resize or hide images to cater to varying screen form factors. Carson will take care of loading an image over the network in varying sizes automatically. It currently supports PNG and JPEG formats."
)
