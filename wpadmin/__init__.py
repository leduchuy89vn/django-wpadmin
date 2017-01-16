"""
django_wpadmin is a collection of extensions/tools for the default Django
administration panel which makes it look and behave more like WordPress
administration panel.
"""
VERSION = (1, 7, 4)

try:
    from django import VERSION as DJANGO_VERSION
except ImportError:
    pass
