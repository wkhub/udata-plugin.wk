# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from udata.tasks import job

log = logging.getLogger(__name__)


@job('{{ .ctx.identifier }}-test-job')
def my_job(self):
    # Implement you first job here
    log.info('Currently working')
