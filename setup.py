# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='myapp',
    version='1.0.0',
    description='Example application for testing multi-stage python builds',
    long_description=readme,
    author='Martin Schuh',
    author_email='development@rebouny.net',
    entry_points={
        "console_scripts": [
            "myapp = myapp.__main__:main"
            ]
    }
)