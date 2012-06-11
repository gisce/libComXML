# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101
# pylint: disable=C0111

from ..core import XmlModel, XmlField

from libcomxml.messages.switching import Cabecera, IdCliente


class DatosSolicitud(XmlModel):
    _sort_order = ('datos', 'linea', 'solicitudadm', 'activacionlectura',
                   'fechaprevista', 'sustituto')
    
    def __init__(self):
        self.datos = XmlField('DatosSolicitud')
        self.linea = XmlField('LineaNegocioElectrica')
        self.solicitudadm = XmlField('SolicitudAdmContractual')
        self.activacionlectura = XmlField('IndActivacionLectura')
        self.fechaprevista = XmlField('FechaPrevistaAccion')
        self.sustituto = XmlField('IndSustitutoMandatario') 
        super(DatosSolicitud, self).__init__('DatosSolicitud', 'datos')


class DireccionCorrespondencia(XmlModel):
    _sort_order = ('direccion', 'indicador')

    def __init__(self):
        self.direccion = XmlField('DireccionCorrespondencia')
        self.indicador = XmlField('Indicador')
        super(DireccionCorrespondencia, self).\
                        __init__('DireccionCorrespondencia', 'direccion')


class IdContrato(XmlModel):
    _sort_order = ('idcontrato', 'codigo')

    def __init__(self):
        self.idcontrato = XmlField('IdContrato')
        self.codigo = XmlField('CodContrato')
        super(IdContrato, self).__init__('IdContrato', 'idcontrato')


class PotenciasContratadas(XmlModel):
    _sort_order = ('potencies', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8',
                   'p9', 'p10')

    def __init__(self):
        self.potencies = XmlField('PotenciasContratadas')
        self.p1 = XmlField('Potencia', attributes={'Periodo': '1'})
        self.p2 = XmlField('Potencia', attributes={'Periodo': '2'})
        self.p3 = XmlField('Potencia', attributes={'Periodo': '3'})
        self.p4 = XmlField('Potencia', attributes={'Periodo': '4'})
        self.p5 = XmlField('Potencia', attributes={'Periodo': '5'})
        self.p6 = XmlField('Potencia', attributes={'Periodo': '6'})
        self.p7 = XmlField('Potencia', attributes={'Periodo': '7'})
        self.p8 = XmlField('Potencia', attributes={'Periodo': '8'})
        self.p9 = XmlField('Potencia', attributes={'Periodo': '9'})
        self.p10 = XmlField('Potencia', attributes={'Periodo': '10'})
        super(PotenciasContratadas, self).\
                             __init__('PotenciasContratadas', 'potencies')


class CondicionesContractuales(XmlModel):
    _sort_order = ('condicions', 'tarifa', 'potencies')

    def __init__(self):
        self.condicions = XmlField('CondicionesContractuales')
        self.tarifa = XmlField('TarifaATR')
        self.potencies = PotenciasContratadas()
        super(CondicionesContractuales, self).\
                             __init__('CondicionesContractuales', 'condicions')


class Contrato(XmlModel):
    _sort_order = ('contrato', 'idcontrato', 'tipo', 'condiciones', 'duracion',
                   'fechafin', 'direccion', 'consumoanual', 
                   'tipoactivacion', 'fechaactivacion')

    def __init__(self):
        self.contrato = XmlField('Contrato')
        self.idcontrato = IdContrato()
        self.duracion = XmlField('Duracion')
        self.fechafin = XmlField('FechaFinalizacion')
        self.tipo = XmlField('TipoContratoATR')
        self.direccion = DireccionCorrespondencia()
        self.consumoanual = XmlField('ConsumoAnualEstimado')
        self.tipoactivacion = XmlField('TipoActivacionPrevista')
        self.fechaactivacion = XmlField('FechaActivacionPrevista')
        self.condiciones = CondicionesContractuales()
        super(Contrato, self).__init__('Contrato', 'contrato')


class Nombre(XmlModel):
    _sort_order = ('nombre', 'nombrepila', 'apellido1','apellido2', 'razon')

    def __init__(self):
        self.nombre = XmlField('Nombre')
        self.nombrepila = XmlField('NombreDePila')
        self.apellido1 = XmlField('PrimerApellido')
        self.apellido2 = XmlField('SegundoApellido')
        self.razon = XmlField('RazonSocial')
        super(Nombre, self).__init__('Nombre', 'nombre')


class Telefono(XmlModel):
    _sort_order = ('telefono', 'prefijo', 'numero')
        
    def __init__(self):
        self.telefono = XmlField('Telefono')
        self.prefijo = XmlField('PrefijoPais')
        self.numero = XmlField('Numero')
        super(Telefono, self).__init__('Telefono', 'telefono')


class Cliente(XmlModel):
    _sort_order = ('cliente', 'idcliente', 'nombre', 'telefono')

    def __init__(self):
        self.cliente = XmlField('Cliente')
        self.idcliente = IdCliente()
        self.nombre = Nombre()
        self.telefono = Telefono()
        super(Cliente, self).__init__('Cliente', 'cliente')


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


class MensajeCambiodeComercializadoraSinCambios(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'cambio')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField('MensajeCambiodeComercializadoraSinCambios', 
                          attributes={
                              'xmlns': 'http://localhost/elegibilidad'
                           })
        self.cabecera = Cabecera()
        self.cambio = CambiodeComercializadoraSinCambios()
        super(MensajeCambiodeComercializadoraSinCambios, self).\
               __init__('MensajeCambiodeComercializadoraSinCambios', 'mensaje')

    def set_agente(self, agente):
        self.mensaje.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()


class DatosAceptacion(XmlModel):
    _sort_order = ('datos', 'fecha', 'potencia', 'actuacion', 'ultlect')
    
    def __init__(self):
        self.datos = XmlField('DatosAceptacion')
        self.fecha = XmlField('FechaAceptacion')
        self.potencia = XmlField('PotenciaActual')
        self.actuacion = XmlField('ActuacionCampo')
        self.ultlect = XmlField('FechaUltimaLectura')
        super(DatosAceptacion, self).__init__('DatosAceptacion', 'datos')


class AceptacionCambiodeComercializadoraSinCambios(XmlModel):
    _sort_order = ('acceptacio', 'dades', 'contracte')

    def __init__(self):
        self.acceptacio = \
                       XmlField('AceptacionCambiodeComercializadoraSinCambios')
        self.dades = DatosAceptacion()
        self.contracte = Contrato()
        super(AceptacionCambiodeComercializadoraSinCambios, self).\
         __init__('AceptacionCambiodeComercializadoraSinCambios', 'acceptacio')


class MensajeAceptacionCambiodeComercializadoraSinCambios(XmlModel):
    _sort_order = ('missatge', 'capcalera', 'acceptacio')
    
    def __init__(self):
        self.doc_root = None
        self.missatge = XmlField('MensajeAceptacionCambiodeComercializadoraSinCambios',
                         attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.capcalera = Cabecera()
        self.acceptacio = AceptacionCambiodeComercializadoraSinCambios() 
        super(MensajeAceptacionCambiodeComercializadoraSinCambios, self).\
                __init__('MensajeAceptacionCambiodeComercializadoraSinCambios',
                         'missatge')
        
    def set_agente(self, agente):
        self.missatge.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()


class Rechazo(XmlModel):
    _sort_order = ('rechazo', 'secuencial', 'motiu', 'text', 'data', 'hora',
                   'idcontracte')
    
    def __init__(self):
        self.rechazo = XmlField('Rechazo')
        self.secuencial = XmlField('Secuencial')
        self.motiu = XmlField('CodigoMotivo', rep=lambda x: x.rjust(2, '0'))
        self.text = XmlField('Texto')
        self.data = XmlField('Fecha')    
        self.hora = XmlField('Hora')
        self.idcontracte = IdContrato()
        super(Rechazo, self).__init__('Rechazo', 'rechazo')

 
class RechazoATRDistribuidoras(XmlModel):
    _sort_order = ('rechazoatr', 'rebuig')

    def __init__(self):
        self.rechazoatr = XmlField('RechazoATRDistribuidoras')
        self.rebuig = Rechazo()
        super(RechazoATRDistribuidoras, self).\
                __init__('RechazoATRDistribuidoras', 'rechazoatr')


class MensajeRechazoATRDistribuidoras(XmlModel):
    _sort_order = ('missatge', 'capcalera', 'rebuig')
    
    def __init__(self):
        self.doc_root = None
        self.missatge = XmlField('MensajeRechazoATRDistribuidoras',
                     attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.capcalera = Cabecera()
        self.rebuig = RechazoATRDistribuidoras()
        super(MensajeRechazoATRDistribuidoras, self).\
                     __init__('MensajeRechazoATRDistribuidoras', 'missatge')

    def set_agente(self, agente):
        self.missatge.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()


class DatosActivacion(XmlModel):
    _sort_order = ('dades', 'data', 'hora')
    
    def __init__(self):
        self.dades = XmlField('DatosActivacion')
        self.data = XmlField('Fecha')
        self.hora = XmlField('Hora')
        super(DatosActivacion, self).__init__('DatosActivacion', 'dades')


class ActivacionCambiodeComercializadoraSinCambios(XmlModel):
    _sort_order = ('activacio', 'dades', 'contracte')
    
    def __init__(self):
        self.activacio = XmlField('ActivacionCambiodeComercializadoraSinCambios')
        self.dades = DatosActivacion()
        self.contracte = Contrato()
        super(ActivacionCambiodeComercializadoraSinCambios, self).\
                __init__('ActivacionCambiodeComercializadoraSinCambios', 'activacio')


class MensajeActivacionCambiodeComercializadoraSinCambios(XmlModel):
    _sort_order = ('missatge', 'capcalera', 'activacio')

    def __init__(self):
        self.doc_root = None
        self.missatge = XmlField('MensajeActivacionCambiodeComercializadoraSinCambios',
                     attributes={'xmlns': 'http://localhost/elegibilidad'})
        self.capcalera = Cabecera()
        self.activacio = ActivacionCambiodeComercializadoraSinCambios()
        super(MensajeActivacionCambiodeComercializadoraSinCambios, self).\
                     __init__('MensajeActivacionCambiodeComercializadoraSinCambios', 'missatge')

    def set_agente(self, agente):
        self.missatge.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()
    
