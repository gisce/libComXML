# -*- coding: utf-8 -*-

from ..core import XmlModel, XmlField

from libcomxml.messages.switching import Cabecera
from sw_c1 import DatosSolicitud, Contrato, Cliente, DatosAceptacion
from sw_c1 import DatosActivacion, PuntosDeMedida
from sw_c2 import Medida, Comentarios, RegistrosDocumento

class BajaEnergia(XmlModel):
    _sort_order = ('cambio', 'solicitud', 'contrato', 'cliente',
                   'comentario', 'registro')

    def __init__(self):
        self.cambio = XmlField('BajaEnergia')
        self.solicitud = DatosSolicitud()
        self.contrato = Contrato()
        self.cliente = Cliente()
        self.comentario = Comentarios()
        self.registro = RegistrosDocumento()
        super(BajaEnergia, self).\
                    __init__('BajaEnergia', 'cambio')
                    
class MensajeBajaEnergia(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'cambio')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField('MensajeBajaEnergia', 
                          attributes={
                              'xmlns': 'http://localhost/elegibilidad'
                           })
        self.cabecera = Cabecera()
        self.cambio = BajaEnergia()
        super(MensajeBajaEnergia, self).\
               __init__('MensajeBajaEnergia', 'mensaje')

    def set_agente(self, agente):
        self.mensaje.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()