# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from flask import url_for

from udata.tests.helpers import assert200

pytestmark = [
    pytest.mark.usefixtures('clean_db'),
    pytest.mark.options(PLUGINS=['{{ identifier }}']),
    pytest.mark.frontend,
]


def test_some_endpoint(client):
    url = url_for('{{ identifier }}.some_endpoint')
    assert200(client.get(url))

# TODO: more testing
