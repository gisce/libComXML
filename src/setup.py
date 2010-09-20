#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os
import re
from distutils.core import setup, Command
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean

KNOWN_XSD = ['Facturacion.xsd', 
             'CambiodeComercializadoraSinCambios.xsd']

class BuildBindings(Command):
    def __init__(self, dist):
        self.build_base = None
        self.known_xsd = None
        Command.__init__(self, dist)
        
    description = "Build bindings for XSDs"
    user_options = []
    
    def initialize_options (self):
        self.build_base = None
        self.known_xsd = KNOWN_XSD[:]

    def finalize_options (self):
        if self.build_base is None:
            self.build_base = 'build'

    def run (self):
        module_path = 'libcomxml.bindings'
        file_package = open('%s%s__init__.py' %
                            (module_path.replace('.', os.path.sep), 
                             os.path.sep), 'w')
        file_package.write('# -*- coding: utf-8 -*-\n')
        for xsd_file in self.known_xsd:
            print "Building module for %s..." % xsd_file
            module_name = '%s.%s' % (module_path, xsd_file.strip('.xsd'))
            xsd = 'libcomxml/xsd/%s' % xsd_file
            # Ugly using os.system(), but there was an error importing
            # pyxb.bindings.generate with more than one xsd file.
            os.system('pyxbgen -m %s %s' % (module_name, xsd))
            # We have to write __init__.py import sentences for every
            # binding generated
            file_package.write('import %s\n' % xsd_file.strip('.xsd'))
        file_package.close()
            
                
class Build(_build):
    def run(self):
        self.run_command('build_bindings')
        _build.run(self)
        
class Clean(_clean):
    def run(self):
        _clean.run(self)
        if os.path.exists(self.build_base):
            print "Cleaning %s dir" % self.build_base
            shutil.rmtree(self.build_base)
        print "Removing generated bindings..."
        package = 'libcomxml.bindings'
        package_file = open('%s%s__init__.py' %
                            (package.replace('.', os.path.sep),
                             os.path.sep), 'w')
        package_file.write('# -*- coding: utf-8 -*-\n')
        package_file.close()
        
        for xsd in KNOWN_XSD:
            module = '%s.%s' % (package, xsd.strip('.xsd'))
            python_file = module.replace('.', os.path.sep)
            if os.path.exists(python_file):
                os.unlink(python_file)

PACKAGES = ['libcomxml', 
            'libcomxml.bindings', 
            'libcomxml.generators', 
            'libcomxml.models', 
            'libcomxml.xsd']
PACKAGES_DATA = {'libcomxml.xsd': []}

XSD_RE = re.compile('^.*\.xsd$')
XSD_DIR = os.path.sep.join('libcomxml.xsd'.split('.'))

XSD_FILELIST = []
# loop on all files and select files matching 'regx'
for root, dirs, files in os.walk(XSD_DIR):
    for name in files:
        if XSD_RE.search(name):
            path = os.path.join(root, name)
            XSD_FILELIST.append(path)

PACKAGES_DATA.update({XSD_DIR.replace(os.path.sep, '.'): XSD_FILELIST})

setup(name='libcomxml',
      description = 'libcomxml is Python package that generates Python source \
      code for classes that correspond to data structures defined by OCSUM',
      author='GISCE Enginyeria',
      author_email='devel@gisce.net',
      url='http://www.gisce.net',
      version='1.14.0',
      license='General Public Licence 2',
      long_description='''Long description''',
      provides=['libcomxml'],
      requires=['PyXB(==1.0.0)'],
      packages=PACKAGES,
      package_data=PACKAGES_DATA,
      scripts=[],
      cmdclass = {'build' : Build, 
                  'clean': Clean, 
                  'build_bindings': BuildBindings})
        
