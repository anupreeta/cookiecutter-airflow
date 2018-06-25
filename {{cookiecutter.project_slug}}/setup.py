#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
import shutil

from pathlib import Path

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


DAG_FILE = '{{cookiecutter.dag_module_name}}.py'
DAG_FILE_PATH = Path(f'./{{cookiecutter.project_slug}}/{DAG_FILE}')

AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
DAGS_FOLDER_PATH = Path(f'{AIRFLOW_HOME}/dags/{DAG_FILE}')


def _copy_dag_file(symlink=False):
    if symlink:
        os.symlink(DAG_FILE_PATH.absolute(), DAGS_FOLDER_PATH)
    else:
        shutil.copy(DAG_FILE_PATH, DAGS_FOLDER_PATH)


class PostDevelopCommand(develop):
    def run(self):
        _copy_dag_file(symlink=True)
        develop.run(self)


class PostInstallCommand(install):
    def run(self):
        _copy_dag_file()
        install.run(self)


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0', {%- endif %}
    {%- if cookiecutter.use_sqlalchemy == 'y' %}
    'SQLAlchemy==1.2.8',
    'psycopg2-binary==2.7.4', {% endif %}
    {%- if cookiecutter.use_rows == 'y' %}
    'rows==0.3.1', {% endif %}
]

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner', {%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest', {%- endif %} ]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        {%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
        {%- endif %}
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    install_requires=requirements,
    {%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
    {%- endif %}
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name='{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    zip_safe=False,
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand
    },
)
