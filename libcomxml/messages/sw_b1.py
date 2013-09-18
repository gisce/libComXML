# -*- coding: utf-8 -*-

from ..core import XmlModel, XmlField

from libcomxml.messages.switching import Cabecera
from sw_c1 import DatosSolicitud, Cliente, DireccionCorrespondencia
from sw_c1 import IdContrato
from sw_c2 import Comentarios, RegistrosDocumento

class BajaEnergia(XmlModel):
    _sort_order = ('cambio', 'solicitud', 'cliente', 'idcontrato',
                   'direccion', 'comentario', 'registro')

    def __init__(self):
        self.cambio = XmlField('BajaEnergia')
        self.solicitud = DatosSolicitud()
        self.cliente = Cliente()
        self.idcontrato = IdContrato()
        self.direccion = DireccionCorrespondencia()
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