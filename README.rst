===============================
django-migration-checker
===============================


.. image:: https://img.shields.io/pypi/v/django_migration_checker.svg
        :target: https://pypi.python.org/pypi/django_migration_checker

.. image:: https://img.shields.io/travis/tonyo/django-migration-checker.svg
        :target: https://travis-ci.org/tonyo/django-migration-checker

.. image:: https://coveralls.io/repos/github/tonyo/django-migration-checker/badge.svg?branch=master
        :target: https://coveralls.io/github/tonyo/django-migration-checker?branch=master

Note: this project is not actively maintained. It's also kind of an ugly hack, and most probably there are better ways to solve the same problem these days. 
---------------------------------------------------------------------------------------------------------------------------------------------------------------

The package allows to detect migration conflicts in Django_ application via static code analysis. In other words, it doesn't run or import any of your code, but finds and parses Django migration files.

The package should work fine with Python 3.6+, and migrations generated by Django 1.7 and later.

**Example:**

::

  >>> from django_migration_checker import get_conflicts
  >>> get_conflicts(app_dir='./django-project/apps')
  [('accounts', ['0001_initial', '0002_new_migration'])]

* Free software: MIT license


Installation
------------

::

  pip install django-migration-checker

Why?
----

The initial goal was to have some way to quickly analyze pull requests to a Django project and detect if the new changes introduce migration conflicts if they are merged to ``master``. 

Here are a few features:

* Fast

  No database connections, heavy modules loading, or checks are performed, so why would it be slow?

* No up-to-date environment needed

  You don't need to have a working Django environment (valid ``settings.py`` file, all installed dependencies, etc.) to use this package. The only requirement is to have properly generated migration files.

* No dependencies

  The package doesn't require Django itself, NumPy, left-pad, or any other packages. 


Command-line tool
-----------------

After installing the package you can use the command-line script ``django-find-conflicts`` to detect migration conflicts from your console.

Here's how it looks like:

::

  $ django-find-conflicts ./django-project/apps
  [('accounts', ['0001_initial', '0002_new_migration'])]

  $ django-find-conflicts ./another-django-project/apps
  No conflicts detected.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Django: https://www.djangoproject.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
