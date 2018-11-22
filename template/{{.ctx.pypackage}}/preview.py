# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from udata.core.dataset.preview import PreviewPlugin


class {{ .ctx.identifier | title | replace "-" "" }}Preview(PreviewPlugin):
    def can_preview(self, resource):
        # Implement here the logic to determinate wether or not you can display a preview
        return False

    def preview_url(self, resource):
        # Compute here the preview URL associated to the given resource
        return 'http://somwhere.com/some/preview/url'
