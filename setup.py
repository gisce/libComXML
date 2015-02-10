# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='libComXML',
    version='2.1.1',
    url='https://github.com/gisce/libComXML',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=['lxml'],
    license='None',
    description='libComXML',
    long_description=open('README.md').read(),
)
