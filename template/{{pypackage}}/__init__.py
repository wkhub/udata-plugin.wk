# -*- coding: utf-8 -*-
'''
{{ project_name }}

{{ description }}
'''
from __future__ import unicode_literals

__version__ = '{{ version }}'
__description__ = '{{ description }}'
{% if features.Has('generic') %}


def init_app(app):
    # Do whatever you want to initialize your plugin
    pass
{% endif %}
