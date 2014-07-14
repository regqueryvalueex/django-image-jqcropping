# -*- coding: utf-8 -*-
from django import template
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer
from django.conf import settings

register = template.Library()


@register.simple_tag
def cropping(obj, crop_field="crop"):
    crop = getattr(obj, crop_field)
    try:
        field = getattr(obj, crop.image_field)
    except AttributeError:
        return getattr(settings, 'DEFAULT_IMAGE_URL', "")
    try:
        return get_thumbnailer(field).get_thumbnail({
            'size': crop.size,
            'box': obj.crop.box,
            'crop': True,
            'detail': True,
        }).url
    except InvalidImageFormatError:
        return ""
