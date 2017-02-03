#!/usr/bin/env python
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

test_requirements = [
]

setup(
    name='django-migration-checker',
    version='0.4.1',
    description="Static migration conflict checker for Django",
    long_description=readme + '\n\n' + history,
    author="Anton Ovchinnikov",
    author_email='anton.ovchi2nikov@gmail.com',
    url='https://github.com/rev112/django-migration-checker',
    packages=[
        'django_migration_checker',
        'django_migration_checker.cli',
    ],
    entry_points={
        'console_scripts': [
            'django-find-conflicts=django_migration_checker.cli.find_conflicts:main',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='django_migration_checker',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
