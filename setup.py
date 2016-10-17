# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='libComXML',
    version='2.2.5',
    url='https://github.com/gisce/libComXML',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=['lxml'],
    license='None',
    description='This library permits XML generation from Python objects',
    test_suite='tests'
)
