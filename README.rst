===============================
django-migration-checker
===============================


.. image:: https://img.shields.io/pypi/v/django_migration_checker.svg
        :target: https://pypi.python.org/pypi/django_migration_checker

.. image:: https://img.shields.io/travis/rev112/django-migration-checker.svg
        :target: https://travis-ci.org/rev112/django-migration-checker


The package allows to detect migration conflicts in Django application via static code analysis.

Example:

```
>>> from django_migration_checker import get_conflicts
>>> get_conflicts(app_dir='./django-project/apps')
[('accounts', ['0001_initial', '0002_new_migration'])]
```

* Free software: MIT license


Installation
------------

```
pip install django-migration-checker
```

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

