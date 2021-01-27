=============================
Django DateAdd
=============================

.. image:: https://badge.fury.io/py/django-dateadd.svg
    :target: https://badge.fury.io/py/django-dateadd

.. image:: https://travis-ci.org/pretix/django-dateadd.svg?branch=master
    :target: https://travis-ci.org/pretix/django-dateadd

.. image:: https://codecov.io/gh/pretix/django-dateadd/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pretix/django-dateadd

DateAdd database function

Documentation
-------------

The full documentation is at https://django-dateadd.readthedocs.io.

Quickstart
----------

Install Django DateAdd::

    pip install django-dateadd

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_dateadd.apps.DjangoDateAddConfig',
        ...
    )

Add Django DateAdd's URL patterns:

.. code-block:: python

    from django_dateadd import urls as django_dateadd_urls


    urlpatterns = [
        ...
        url(r'^', include(django_dateadd_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
