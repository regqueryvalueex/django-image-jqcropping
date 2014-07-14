from django import forms
from django.utils.safestring import mark_safe


class JQCropWidget(object):
    class Media:
        js = (
            "cropper-master/js/jquery-1.11.1.min.js",
            "cropper-master/js/cropper.min.js",
            "cropper-master/js/modal.js",
        )
        css = {'all': ("cropper-master/css/cropper.min.css",
                       "cropper-master/css/modal.css",)}


class ImageJQCropWidget(forms.ClearableFileInput, JQCropWidget):
    url_markup_template = '<a target="_blank" href="{0}" data-name="%s" class="crop-dialog-open"><img src="{0}" alt="{1}"/></a>'

    def __init__(self, *args, **kwargs):
        super(forms.ClearableFileInput, self).__init__(*args, **kwargs)
        try:
            self.attrs['class'] += " img-cropping"
        except KeyError:
            self.attrs['class'] = "img-cropping"

    def render(self, name, value, attrs=None):
        self.url_markup_template = self.url_markup_template % name
        return super(ImageJQCropWidget, self).render(name, value, attrs)


class ImageJQCropInfoFormWidget(forms.widgets.MultiWidget):

    is_hidden = True

    def __init__(self, image_field, size, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        self.image_field = image_field
        self.size = size
        _widgets = (forms.widgets.NumberInput(),)*6
        super(ImageJQCropInfoFormWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.x1, value.y1, value.width, value.height, value.x2, value.y2]
        return [None, ]*6

    def render(self, name, value, attrs=None):
        tmp = super(ImageJQCropInfoFormWidget, self).render(name, value, attrs)
        block_attrs = (u'id="%s-crop"'% self.image_field,
                       u'data-size="%s"'% self.size,
                       u'data-name="%s"'% name,
                       u'data-contain-hidden-fields',
        )

        return mark_safe (u'<div {0}>{1}<div id="{2}-img-crop" class="cropping-block"></div></div>'.format(
            u' '.join(block_attrs), tmp, self.image_field))