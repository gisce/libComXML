#!/usr/bin/env python
version = '1.14.0'

import sys

from distutils.core import Command

class build_bindings(Command):
    import pyxb.binding.generate
    known_xsd = ['Facturacion.xsd', 'AceptacionAnulacion.xsd']
    known_xsd_str = '* '+'\n* '.join(known_xsd)
    description = "Build bindings for known XSDs:\n %s" % (known_xsd_str)
    for xsd_file in known_xsd:
        print "Building module for %s..." % xsd_file
        module = 'libComXML.bindings.%s' % xsd_file.strip('.xsd')
        xsd = 'libComXML/xsd/%s' % xsd_file
        generator = pyxb.binding.generate.Generator()
        print generator.generationUID()
        generator.addModuleName(module)
        generator.setSchemaLocationList([xsd])
        generator.resolveExternalSchema()
        try:
            tns = generator.namespaces().pop()
            modules = generator.bindingModules()
            print 'Python for %s requires %d modules' % (tns, len(modules))
            top_module = None
            path_dirs = set()
            for m in modules:
                m.writeToModuleFile()
            generator.writeNamespaceArchive()
        except Exception, e:
            print 'Exception generating bindings: %s' % (e,)
            sys.exit(3)
        
