# -*- coding: utf-8 -*-
from libComXML.bindings import Facturacion
from libComXML.models import Factura

class FacturaGenerator(object):
    
    def __init__(self):
        self.binding = None
        self.factures = []
        pass
    
    def generate_from_binding(self, binding):
        self.binding = binding
        self.generateFactures()
        return self.factures
    
    def generate_from_xml(self, xml_text):
        self.binding = Facturacion.CreateFromDocument(xml_text)
        self.generateFactures()
        return self.factures

    def _generate_factures(self):
        for f in self.binding.Facturas.FacturaATR:
            factura = Factura()
            factura.nif_client = f.DatosGeneralesFacturaATR.Cliente.Identificador
            factura.contracte = f.DatosGeneralesFacturaATR.Contrato
            factura.numero = f.DatosGeneralesFacturaATR.DatosGeneralesFactura.NumeroFactura
            factura.tipus = f.DatosGeneralesFacturaATR.DatosGeneralesFactura.TipoFactura
            factura.rectificativa = f.DatosGeneralesFacturaATR.DatosGeneralesFactura.IndicativoFacturaRectificadora
            factura.data_factura = f.DatosGeneralesFacturaATR.DatosGeneralesFactura.FechaFactura
        self.factures.append(f)