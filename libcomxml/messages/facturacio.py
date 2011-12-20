# -*- coding: utf-8 -*-

from ..core import XmlModel, XmlField

class Cabecera(XmlModel):
    _sort_order = ('cabecera', 'ree_emisora', 'ree_destino', 'proceso', 'paso',
                   'solicitud', 'secuencia', 'codigo', 'fecha', 'version')
    cabecera = XmlField('Cabecera')
    ree_emisora = XmlField('CodigoREEEmpresaEmisora')
    ree_destino = XmlField('CodigoREEEmpresaDestino')
    proceso = XmlField('CodigoDelProceso')
    paso = XmlField('CodigoDelPaso')
    solicitud = XmlField('CodigoDeSolicitud')
    secuencia = XmlField('SecuencialDeSolicitud')
    codigo = XmlField('Codigo')
    fecha = XmlField('FechaSolicitud')
    version = XmlField('Version', value='02')


class DatosGeneralesFactura(XmlModel):
    _sort_order = ('datos', 'numero', 'tipo', 'rectificadora', 'fecha', 'cif',
                   'codigo', 'obs', 'importe', 'saldo', 'saldocobro', 'moneda')
    datos = XmlField('DatosGeneralesFactura')
    numero = XmlField('NumeroFactura')
    tipo = XmlField('TipoFactura')
    rectificadora = XmlField('IndicativoFacturaRectificadora')
    fecha = XmlField('FechaFactura')
    cif = XmlField('CIFEmisora')
    codigo = XmlField('CodigoFiscalFactura')
    obs = XmlField('Observaciones')
    importe = XmlField('Importe')
    saldo = XmlField('SaldoFactura')
    saldocobro = XmlField('SaldoCobro')
    moneda = XmlField('TipoMoneda', value='02')


class Periodo(XmlModel):
    _sort_order = ('periodo', 'fecha_desde', 'fecha_hasta', 'meses')
    periodo = XmlField('Periodo')
    fecha_desde = XmlField('FechaDesdeFactura')
    fecha_hasta = XmlField('FechaHastaFactura')
    meses = XmlField('NumeroMeses')


class DatosFacturaATR(XmlModel):
    _sort_order = ('datos', 'tipo', 'boe', 'tarifa', 'imab', 'periodo')
    datos = XmlField('DatosFacturaATR')
    tipo = XmlField('TipoFacturacion')
    boe = XmlField('FechaBOE')
    tarifa = XmlField('CodigoTarifa')
    imab = XmlField('IndAltamedidoenBaja')
    periodo = Periodo('Periodo', root='periodo')


class DireccionSuministro(XmlModel):
    _sort_order = ('direccion', 'cups', 'municipio', 'dirsuministro')
    direccion = XmlField('DireccionSuministro')
    cups = XmlField('CUPS')
    municipio = XmlField('Municipio')
    dirsuministro = XmlField('DirSuministro')

class Cliente(XmlModel):
    _sort_order = ('cliente', 'cifnif', 'identificador')
    cliente = XmlField('Cliente')
    cifnif = XmlField('TipoCIFNIF')
    identificador = XmlField('Identificador')

class DatosGeneralesFacturaATR(XmlModel):
    _sort_order = ('datos', 'direccion', 'cliente', 'contrato', 'datosgrles',
                   'datosatr')
    datos = XmlField('DatosGeneralesFacturaATR')
    direccion = DireccionSuministro('DireccionSuministro', root='direccion')
    cliente = Cliente('Cliente', root='cliente')
    contrato = XmlField('Contrato')
    datosgrles = DatosGeneralesFactura('DatosGeneralesFactura', root='datos')
    datosatr = DatosFacturaATR('DatosFacturaATR', root='datos')


class FacturaATR(XmlModel):
    _sort_order = ('factura', 'datosatr')
    factura = XmlField('FacturaATR')
    datosatr = DatosGeneralesFacturaATR('DatosGeneralesFacturaATR',
                                        root='datos')

class MensajeFacturacion(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'facturas')
    mensaje = XmlField('MensajeFacturacion', attributes={
                       'xmlns': 'http://localhost/elegibilidad'})
    cabecera = Cabecera('Cabecera', root='cabecera')
    facturas = XmlField('Facturas')

    def set_agente(self, agente):
        self.mensaje.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()

