<h2>Installation</h2>
Install django-image-jqcropping using <tt>pip</tt>:
<pre>pip install django-image-jqcropping</pre>
<h2>Usage</h2>
<p>Add <tt>easy_thumbnails</tt> and <tt>image_cropping</tt> to your INSTALLED_APPS</p>

<p>In Your <tt>models.py</tt></p>

<pre>
from django.db import models
from image_jqcropping import ImageJQCropInfoField

class Content(models.Model):
    image = models.ImageField(u'Аватар', upload_to='accounts/avatar/%Y/%m/', blank=True, null=True, max_length=1000)
    crop  = ImageJQCropInfoField(verbose_name=u'Обрезка', image_field='image', size="300x400", blank=True, null=True)
</pre>

<p>In templates</p>

<pre>
{% load jqcropping %}

&lt;img src="{% cropping contentinstance 'crop' %}" height="50px" /&gt;
</pre>

<h2>Screenshot:</h2>
<img src="http://cdn.joxi.ru/uploads/prod/2014/07/14/9bc/960/9543f8e1d7afcf1a76ac846a25e44e68b6246c0c.jpg" />
