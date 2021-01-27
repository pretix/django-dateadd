=====
Usage
=====

To use Django DateAdd in a project, add it to your `INSTALLED_APPS`:

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
