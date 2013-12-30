# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='libComXML',
    version='2.0.0',
    url='http://git.gisce.lan/libComXML.git',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=['lxml'],
    license='None',
    description='libComXML',
    long_description=open('README.md').read(),
)
