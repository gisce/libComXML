# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101
# pylint: disable=C0111

from ..core import XmlModel, XmlField

from libcomxml.messages.switching import Cabecera, Cliente


class DatosSolicitud(XmlModel):
    _sort_order = ('datos', 'linea', 'solicitudadm', 'activacionlectura',
                   'sustituto')
    
    def __init__(self):
        self.datos = XmlField('DatosSolicitud')
        self.linea = XmlField('LineaNegocioElectrica')
        self.solicitudadm = XmlField('SolicitudAdmContractual')
        self.activacionlectura = XmlField('IndActivacionLectura')
        self.sustituto = XmlField('IndSustitutoMandatario') 
        super(DatosSolicitud, self).__init__('DatosSolicitud', 'datos')


class DireccionCorrespondencia():
    _sort_order = ('direccion', 'indicador')

    def __init__(self):
        self.direccion = XmlField('DireccionCorrespondencia')
        self.indicador = XmlField('Indicador')
        super(DireccionCorrespondencia, self).\
                        __init__('DireccionCorrespondencia', 'direccion')


class IdContrato():
    _sort_order = ('idcontrato', 'codigo')

    def __init__(self):
        self.idcontrato = XmlField('IdContrato')
        self.codigo = XmlField('CodContrato')
        super(IdContrato, self).__init__('IdContrato', 'idcontrato')


class Contrato(XmlModel):
    _sort_order = ('contrato', 'idcontrato', 'duracion', 'fechafin', 'tipo',
                   'direccion')

    def __init__(self):
        self.contrato = XmlField('Contrato')
        self.idcontrato = IdContrato()
        self.duracion = XmlField('Duracion')
        self.fechafin = XmlField('FechaFinalizacion')
        self.tipo = XmlField('TipoContratoATR')
        self.direccion = DireccionCorrespondencia()
        super(Contrato, self).__init__('Contrato', 'contrato')


class CambiodeComercializadoraSinCambios(XmlModel):
    _sort_order = ('cambio', 'solicitud', 'contrato', 'cliente', 'aparato', 
                   'comentario', 'registro')

    def __init__(self):
        self.cambio = XmlField('CambiodeComercializadoraSinCambios')
        self.solicitud = DatosSolicitud()
        self.contrato = Contrato()
        self.cliente = Cliente()
        self.aparato = XmlField('ModelosAparato')
        self.comentario = XmlField('Comentarios')
        self.registro = XmlField('RegistrosDocumento')
        super(CambiodeComercializadoraSinCambios, self).\
                    __init__('CambiodeComercializadoraSinCambios', 'cambio', 
                             drop_empty=False)


class CambiodeComercializadoraSinCambios(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'cambio')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField('CambiodeComercializadoraSinCambios', 
                          attributes={
                              'xmlns': 'http://localhost/elegibilidad'
                           })
        self.cabecera = Cabecera()
        self.cambio = CambiodeComercializadoraSinCambios()
        super(MensajeFacturacion, self).__init__('MensajeFacturacion',
                                                 'mensaje')

    def set_agente(self, agente):
        self.mensaje.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()
