#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name     = 'django-image-jqcropping',
    version  = '0.1.0',
    packages = find_packages(),
    requires = ['python (>= 2.7)', 'django (>= 1.6)', 'easy_thumbnails (>=2.0)'],
    description  = 'Application for easy image cropping with django and Jquery.',
    author       = 'Alexandr Zayets',
    author_email = 'alex.consp@gmail.com',
    url          = 'https://github.com/regqueryvalueex/django-image-jqcropping',
    download_url = 'https://github.com/regqueryvalueex/django-image-jqcropping/archive/master.zip',
    keywords     = 'django',
    classifiers  = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)