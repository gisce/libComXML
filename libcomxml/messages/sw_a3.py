# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101
# pylint: disable=C0111

from ..core import XmlModel, XmlField

from libcomxml.messages.switching import Cabecera
from sw_c1 import DatosSolicitud, Contrato, Cliente, DatosAceptacion
from sw_c1 import DatosActivacion, PuntosDeMedida
from sw_c2 import Medida, Comentarios, RegistrosDocumento

class PasoMRAMLConCambiosRestoTarifas(XmlModel):
    _sort_order = ('cambio', 'solicitud', 'contrato', 'cliente',
                   'medida', 'doctecnica', 'comentario', 'registro')
    
    def __init__(self):
        self.cambio= XmlField('PasoMRAMLConCambiosRestoTarifa')
        self.solicitud = DatosSolicitud()
        self.contrato = Contrato()
        self.cliente = Cliente()
        self.cliente_saliente = Cliente()
        self.medida = Medida()
        self.doctecnica = XmlField('DocTecnica')
        self.comentario = Comentarios()
        self.registro = RegistrosDocumento()
        super(PasoMRAMLConCambiosRestoTarifas, self).\
                    __init__('PasoMRAMLConCambiosRestoTarifa', 'cambio')
                    
class MensajePasoMRAMLConCambiosRestoTarifas(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'cambio')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField('MensajePasoMRAMLConCambiosRestoTarifa', 
                          attributes={
                              'xmlns': 'http://localhost/elegibilidad'
                           })
        self.cabecera = Cabecera()
        self.cambio = PasoMRAMLConCambiosRestoTarifas()
        super(MensajePasoMRAMLConCambiosRestoTarifas, self).\
               __init__('MensajePasoMRAMLConCambiosRestoTarifa', 'mensaje')

    def set_agente(self, agente):
        self.mensaje.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()