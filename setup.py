#!/usr/bin/env python
from setuptools import setup


def parse_requirements(requirements, ignore=("setuptools",)):
    """
    Read dependencies from requirements file (with version numbers if any)
    Notes:
        - this implementation does not support requirements files with extra
          requirements
        - this implementation has been taken from TailorDev/Watson's setup file
    """
    with open(requirements) as f:
        packages = set()
        for line in f:
            line = line.strip()
            if line.startswith(("#", "-r", "--")):
                continue
            if "#egg=" in line:
                line = line.split("#egg=")[1]
            pkg = line.strip()
            if pkg and pkg not in ignore:
                packages.add(pkg)
        return list(packages)


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

setup(
    name="django-migration-checker",
    version="0.8.0",
    description="Static migration conflict checker for Django",
    long_description=readme + "\n\n" + history,
    author="Anton Ovchinnikov",
    author_email="anton.ovchi2nikov@gmail.com",
    url="https://github.com/tonyo/django-migration-checker",
    packages=[
        "django_migration_checker",
        "django_migration_checker.cli",
    ],
    entry_points={
        "console_scripts": [
            "django-find-conflicts=django_migration_checker.cli.find_conflicts:main",
        ],
    },
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords="django_migration_checker",
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    test_suite="tests",
    install_requires=[],
    tests_require=parse_requirements("requirements_dev.txt"),
    setup_requires=parse_requirements("requirements_dev.txt"),
)
