#!/usr/bin/env python
import shutil
version = '1.14.0'

import sys
import os
import re
from distutils.core import setup, Command
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean

global know_xsd
known_xsd = ['Facturacion.xsd', 
                'CambiodeComercializadoraSinCambios.xsd']

class build_bindings(Command):
    description = "Build bindings for XSDs"
    
    user_options = []
    
    def initialize_options (self):
        self.build_base = None
        self.known_xsd = known_xsd[:]

    def finalize_options (self):
        if self.build_base is None:
            self.build_base = 'build'

    def run (self):
        module_path = 'libComXML.bindings'
        f = open('%s%s__init__.py'% (module_path.replace('.', os.path.sep), os.path.sep), 'w')
        f.write('# -*- coding: utf-8 -*-\n')
        for xsd_file in self.known_xsd:
            print "Building module for %s..." % xsd_file
            module_name = '%s.%s' % (module_path, xsd_file.strip('.xsd'))
            xsd = 'libComXML/xsd/%s' % xsd_file
            # Ugly using os.system(), but there was an error importing
            # pyxb.bindings.generate with more than one xsd file.
            os.system('pyxbgen -m %s %s' % (module_name, xsd))
            # We have to write __init__.py import sentences for every
            # binding generated
            f.write('import %s\n' % xsd_file.strip('.xsd'))
        f.close()
            
                
class build(_build):
    def run(self):
        self.run_command('build_bindings')
        _build.run(self)
        
class clean(_clean):
    def run(self):
        _clean.run(self)
        if os.path.exists(self.build_base):
            print "Cleaning %s dir" % self.build_base
            shutil.rmtree(self.build_base)
        print "Removing generated bindings..."
        package = 'libComXML.bindings'
        f = open('%s%s__init__.py'% (package.replace('.', os.path.sep), os.path.sep), 'w')
        f.write('# -*- coding: utf-8 -*-\n')
        f.close()
        
        for xsd in known_xsd:
            module = '%s.%s' % (package, xsd.strip('.xsd'))
            python_file = module.replace('.', os.path.sep)
            if os.path.exists(python_file):
                os.unlink(python_file)

packages = ['libComXML', 'libComXML.bindings', 'libComXML.generators', 'libComXML.models', 'libComXML.xsd']
packages_data = {'libComXML.xsd': []}

xsd_re = re.compile('^.*\.xsd$')
xsd_dir = os.path.sep.join('libComXML.xsd'.split('.'))

xsd_fileslist = []
# loop on all files and select files matching 'regx'
for root, dirs, files in os.walk(xsd_dir):
    for name in files:
        if xsd_re.search(name):
            path = os.path.join(root, name)
            xsd_fileslist.append(path)

packages_data.update({xsd_dir.replace(os.path.sep, '.'): xsd_fileslist})

setup(name='libComXML',
      description = 'libComXML is Python package that generates Python source code for classes that correspond to data structures defined by OCSUM',
      author='GISCE Enginyeria',
      author_email='devel@gisce.net',
      url='http://www.gisce.net',
      version=version,
      license='General Public Licence 2',
      long_description='''Long description''',
      provides=['libComXML'],
      requires=['PyXB(==1.0.0)'],
      packages=packages,
      package_data=packages_data,
      scripts=[],
      cmdclass = {'build' : build, 'clean': clean, 'build_bindings': build_bindings})
        
