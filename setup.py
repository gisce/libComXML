# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='libComXML',
    version='1.1.0',
    url='http://git.gisce.lan/libComXML.git',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=['libcomxml', 'libcomxml.core', 'libcomxml.messages',
              'libcomxml.helpers'],
    requires=['lxml'],
    license='None',
    description='libComXML',
    long_description=open('README').read(),
)
