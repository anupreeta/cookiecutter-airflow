{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}


Minimal requirements
--------------------

 - Python >=3.6
 - Docker
 - Docker Compose


Installation
------------

1. Checkout the project

.. code:: bash

    $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git

2. Create the virtualenv and install the dependencies

.. code:: bash

    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements_dev.txt

4. Do the configuration of Airflow

.. code:: bash

    $ make setup_airflow
    $ export AIRFLOW_HOME=$PWD/airflow

4. Install the packate in ``develop`` mode

.. code:: bash

    $ make develop

This is create a simbolic link of module, where have your DAG in Airflow DAG folder.

5. Create the database for development and test using ``docker-compose``

.. code:: bash

    $ docker-compose up -d
    $ export DATABASE_URL=postgresql://{{ cookiecutter.project_slug }}:{{ cookiecutter.project_slug }}@localhost/{{ cookiecutter.project_slug }}_test

6. Run all migrations for create the tables

.. code:: bash

    $ make migrate

7. Run the Airflow panel and/or run your DAG:

.. code:: bash

    $ make run_airflow


.. code:: bash

    $ airflow backfill -s 2018-01-01 dag_integracao_evg_suap -sd airflow/dags


Using direnv
------------

To recognize the variable environment in fast mode, we recommend that use direnv_ for set this values automatically.

.. code:: bash

    $ cp contrib/env-sample .envrc
    $ direnv allow .

This define the variabled ``AIRFLOW_HOME`` and ``DATABASE_URL``.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `gilsondev/cookiecutter-airflow`_ project template.

.. _direnv: https://direnv.net/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`gilsondev/cookiecutter-airflow`: https://github.com/gilsondev/cookiecutter-airflow
