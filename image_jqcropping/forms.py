# -*- coding: utf-8 -*-
from django import forms
from smk.accounts.widgets import ImageJQCropInfoFormWidget


class ImageJQCropInfoFormField(forms.MultiValueField):

    widget = ImageJQCropInfoFormWidget

    def __init__(self, image_field, size, *args, **kwargs):
        self.widget = self.widget(image_field, size)
        fields = (forms.IntegerField(),)*6

        super(ImageJQCropInfoFormField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return u'.'.join([str(x) for x in data_list])
        return None