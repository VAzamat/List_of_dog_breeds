from django import template

from django.conf import settings

import os


register = template.Library()


@register.filter()
def mediapath(path):
    """
    Join the given path with the MEDIA_URL setting.

    Usage::

        {{path_as_string|mediapath}}

    Examples::

        {{"python/Minduka_Present_Blue_Pack.png"|mediapath}}

    """
    fullpath = os.path.join(settings.BASE_DIR, settings.MEDIA_URL, str(path) )
    return fullpath


@register.simple_tag
def get_media_prefix(path):
    """
    Join the given path with the MEDIA_URL setting.

    Usage::

        {% get_media_prefix path [as varname] %}

    Examples:
        {% get_media_prefix "python/Minduka_Present_Blue_Pack.png" %}


    """
    fullpath = os.path.join(settings.BASE_DIR, settings.MEDIA_URL, str(path) )
    return fullpath

