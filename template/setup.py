#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import io
import re

from setuptools import setup, find_packages

RE_BADGE = re.compile(r'^\[\!\[(?P<text>.*?)\]\[(?P<badge>.*?)\]\]\[(?P<target>.*?)\]$', re.M)

BADGES_TO_KEEP = []


def md(filename):
    '''
    Load .md (markdown) file and sanitize it for PyPI.
    '''
    content = io.open(filename).read()

    for match in RE_BADGE.finditer(content):
        if match.group('badge') not in BADGES_TO_KEEP:
            content = content.replace(match.group(0), '')

    return content


def pip(filename):
    """Parse pip reqs file and transform it to setuptools requirements."""
    return open(os.path.join('requirements', filename)).readlines()


long_description = '\n'.join((
    md('README.md'),
    md('CHANGELOG.md'),
    ''
))

install_requires = pip('install.pip')
tests_require = pip('test.pip')


setup(
    name='{{ .ctx.project_slug }}',
    version=__import__('{{ .ctx.pypackage }}').__version__,
    description=__import__('{{ .ctx.pypackage }}').__description__,
    long_description=long_description,
    url='{{ .ctx.website }}',
    author='{{ .ctx.author }}',
    author_email='{{ .ctx.email }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    entry_points={
        {{ if .ctx.features | contains "harvester" -}}
        'udata.harvesters': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.harvesters:{{ .ctx.identifier | title | replace "-" "" }}Backend',
        ],
        {{- end }}
        {{ if .ctx.features | contains "theme" -}}
        'udata.theme': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.theme',
        ],
        {{- end }}
        {{if .ctx.features | contains "views" -}}
        'udata.views': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.views',
        ],
        {{- end }}
        {{if .ctx.features | contains "metrics" -}}
        'udata.metrics': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.metrics',
        ],
        {{- end }}
        {{if .ctx.features | contains "models" -}}
        'udata.models': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.models',
        ],
        {{- end }}
        {{if .ctx.features | contains "linkchecker" -}}
        'udata.linkcheckers': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.linkchecker:{{ .ctx.identifier | title | replace "-" "" }}LinkChecker',
        ],
        {{- end }}
        {{if .ctx.features | contains "tasks" -}}
        'udata.tasks': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.tasks',
        ],
        {{- end }}
        {{if .ctx.features | contains "preview" -}}
        'udata.preview': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}.preview:{{ .ctx.identifier | title | replace "-" "" }}Preview',
        ],
        {{- end }}
        {{if .ctx.features | contains "generic_plugin" -}}
        'udata.plugins': [
            '{{.ctx.identifier}} = {{.ctx.pypackage}}',
        ],
        {{- end }}
    },
    license='{{ .ctx.license }}',
    zip_safe=False,
    keywords='udata, harvester, {{ .ctx.project_name }}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: System :: Software Distribution',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
