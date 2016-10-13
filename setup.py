# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='libComXML',
    version='3.0.1',
    url='https://github.com/gisce/libComXML',
    author='GISCE-TI, S.L',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=['lxml', 'six'],
    license='None',
    description='This library permits XML generation from Python objects',
    test_suite='tests',
    classifiers=[
        'Topic :: Text Processing :: Markup :: XML',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ]
)
