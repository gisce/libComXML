# -*- coding: utf-8 -*-
from libComXML.bindings import Facturacion

class Factura:
    def __init__(self):
        self.binding = None
    
    def parseXML(self, xml_text):
        self.binding = Facturacion.CreateFromDocument(xml_text) 