#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name     = 'django-image-jqcropping',
    version  = '0.1.0',
    packages = find_packages(),
    requires = ['python (>= 2.7)', 'django (>= 1.6)', 'easy-thumbnails (>=2.0)'],
    description  = 'Crop the images.',
    long_description = open('README.markdown').read(), 
    author       = 'Alexandr Zayets',
    author_email = 'alex.consp@gmail.com',
    url          = 'https://github.com/regqueryvalueex/django-image-jqcropping',
    keywords     = 'django',
    classifiers  = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)