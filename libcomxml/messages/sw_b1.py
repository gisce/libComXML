# -*- coding: utf-8 -*-

from ..core import XmlModel, XmlField

from libcomxml.messages.switching import Cabecera
from sw_c1 import DatosSolicitud, Cliente, DireccionCorrespondencia
from sw_c1 import IdContrato, DatosAceptacion
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
        
        
class AceptacionBajaEnergia(XmlModel):
    _sort_order = ('acceptacio', 'dades', 'idcontracte')

    def __init__(self):
        self.acceptacio = XmlField('AceptacionBajaEnergia')
        self.dades = DatosAceptacion()
        self.idcontracte = IdContrato()
        super(AceptacionBajaEnergia, self).\
         __init__('AceptacionBajaEnergia', 'acceptacio')


class MensajeAceptacionBajaEnergia(XmlModel):
    _sort_order = ('missatge', 'capcalera', 'acceptacio')
    
    def __init__(self):
        self.doc_root = None
        self.missatge = XmlField('MensajeAceptacionBajaEnergia',
                         attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.capcalera = Cabecera()
        self.acceptacio = AceptacionBajaEnergia()
        super(MensajeAceptacionBajaEnergia, self).\
                __init__('MensajeAceptacionBajaEnergia',
                         'missatge')
        
    def set_agente(self, agente):
        self.missatge.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()