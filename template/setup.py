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
    name='{{ project_slug }}',
    version=__import__('{{ pypackage }}').__version__,
    description=__import__('{{ pypackage }}').__description__,
    long_description=long_description,
    url='{{ website }}',
    author='{{ author }}',
    author_email='{{ email }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    entry_points={
        {% if features.Has('harvester') -%}
        'udata.harvesters': [
            '{{identifier}} = {{pypackage}}.harvesters:{{ identifier | title | replace("-", "") }}Backend',
        ],
        {%- endif %}
        {% if features.Has('theme') -%}
        'udata.theme': [
            '{{identifier}} = {{pypackage}}.theme',
        ],
        {%- endif %}
        {% if features.Has('views') -%}
        'udata.views': [
            '{{identifier}} = {{pypackage}}.views',
        ],
        {%- endif %}
        {% if features.Has('metrics') -%}
        'udata.metrics': [
            '{{identifier}} = {{pypackage}}.metrics',
        ],
        {%- endif %}
        {% if features.Has('models') -%}
        'udata.models': [
            '{{identifier}} = {{pypackage}}.models',
        ],
        {%- endif %}
        {% if features.Has('linkchecker') -%}
        'udata.linkcheckers': [
            '{{identifier}} = {{pypackage}}.linkchecker:{{ identifier | title | replace("-", "") }}LinkChecker',
        ],
        {%- endif %}
        {% if features.Has('tasks') -%}
        'udata.tasks': [
            '{{identifier}} = {{pypackage}}.tasks',
        ],
        {%- endif %}
        {% if features.Has('preview') -%}
        'udata.preview': [
            '{{identifier}} = {{pypackage}}.preview:{{ identifier | title | replace("-", "") }}Preview',
        ],
        {%- endif %}
        {% if features.Has('generic_plugin') -%}
        'udata.plugins': [
            '{{identifier}} = {{pypackage}}',
        ],
        {%- endif %}
    },
    license='{{ license }}',
    zip_safe=False,
    keywords='udata, harvester, {{ project_name }}',
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
