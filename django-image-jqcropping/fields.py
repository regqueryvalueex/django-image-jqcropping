# -*- coding: utf-8 -*-
from django.db import models
from django.utils.six import with_metaclass
from .forms import ImageJQCropInfoFormField


class ImageJQCropInfo(object):

    def __init__(self, size="300x300", image_field="image", x1=None, y1=None, width=None, height=None, x2=None, y2=None, *args, **kwargs):
        self.x1     = x1
        self.y1     = y1
        self.width  = width
        self.height = height
        self.x2     = x2
        self.y2     = y2
        self.image_field = image_field
        self.size = (int(size.split('x')[0]), int(size.split('x')[1]))

    @property
    def ratio(self):
        return self.size['width']/self.size['height']

    @property
    def box(self):
        return u','.join([str(x) for x in [self.x1,
                                           self.y1,
                                           self.x2,
                                           self.y2]])

    def __str__(self):
        return u'.'.join([str(x) for x in [self.x1,
                                          self.y1,
                                          self.width,
                                          self.height,
                                          self.x2,
                                          self.y2]])

    def __unicode__(self):
        return self.__str__()


class ImageJQCropInfoField(with_metaclass(models.SubfieldBase, models.Field)):

    description = "Info for cropping"

    def __init__(self, size="300x300", image_field='image', *args, **kwargs):
        self.image_field = image_field
        self.size = size
        self.max_length=255
        super(ImageJQCropInfoField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, ImageJQCropInfo):
            return value
        try:
            args = [int(x) for x in value.split('.')]
        except AttributeError:
            return None
        return ImageJQCropInfo(self.size, self.image_field, *args)

    def get_prep_value(self, value):
        try:
            return u'.'.join([str(x) for x in [value.x1,
                                              value.y1,
                                              value.width,
                                              value.height,
                                              value.x2,
                                              value.y2]])
        except AttributeError:
            return None

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': ImageJQCropInfoFormField, 'image_field': self.image_field, 'size':self.size}
        defaults.update(kwargs)
        return super(ImageJQCropInfoField, self).formfield(**defaults)

    def south_field_triple(self):
        """
        Return a suitable description of this field for South.
        """
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.CharField"
        args, kwargs = introspector(self)
        kwargs.update({"max_length":255})
        return field_class, args, kwargs