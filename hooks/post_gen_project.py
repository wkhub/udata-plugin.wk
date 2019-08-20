#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

TO_REMOVE = [
    {% if cookiecutter.has_harvester == 'no' %}'harvesters.py',{% endif %}
    {% if cookiecutter.has_theme == 'no' %}'theme',{% endif %}
    {% if cookiecutter.has_views == 'no' %}'views.py',{% endif %}
    {% if cookiecutter.has_metrics == 'no' %}'metrics.py',{% endif %}
    {% if cookiecutter.has_models == 'no' %}'models.py',{% endif %}
    {% if cookiecutter.has_linkchecker == 'no' %}'linkchecker.py',{% endif %}
    {% if cookiecutter.has_tasks == 'no' %}'tasks.py',{% endif %}
    {% if cookiecutter.has_preview == 'no' %}'preview.py',{% endif %}
]

TESTS_TO_REMOVE = [
    {% if cookiecutter.has_harvester == 'no' %}'test_{{ cookiecutter.identifier.replace('-', '_') }}_backend.py',{% endif %}
    {% if cookiecutter.has_views == 'no' %}'test_{{ cookiecutter.identifier.replace('-', '_') }}_views.py',{% endif %}
    {% if cookiecutter.has_preview == 'no' %}'test_{{ cookiecutter.identifier.replace('-', '_') }}_preview.py',{% endif %}
]


def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
    else:
        os.remove(path)


if __name__ == '__main__':

    # Remove unnecessary files
    for name in TO_REMOVE:
        path = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.pypackage }}', name)
        remove(path)

    for name in TESTS_TO_REMOVE:
        path = os.path.join(PROJECT_DIRECTORY, 'tests', name)
        remove(path)
