# -*- coding: utf-8 -*-
'''
{{ .ctx.project_name }}

{{ .ctx.description }}
'''
from __future__ import unicode_literals

__version__ = '{{ .ctx.version }}'
__description__ = '{{ .ctx.description }}'
{{if .ctx.features | contains "generic" }}


def init_app(app):
    # Do whatever you want to initialize your plugin
    pass
{{ end }}
