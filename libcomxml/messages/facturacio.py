# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101

from ..core import XmlModel, XmlField

class Cabecera(XmlModel):
    _sort_order = ('cabecera', 'ree_emisora', 'ree_destino', 'proceso', 'paso',
                   'solicitud', 'secuencia', 'codigo', 'fecha', 'version')

    def __init__(self, name, root):
        self.cabecera = XmlField('Cabecera')
        self.ree_emisora = XmlField('CodigoREEEmpresaEmisora')
        self.ree_destino = XmlField('CodigoREEEmpresaDestino')
        self.proceso = XmlField('CodigoDelProceso')
        self.paso = XmlField('CodigoDelPaso')
        self.solicitud = XmlField('CodigoDeSolicitud')
        self.secuencia = XmlField('SecuencialDeSolicitud')
        self.codigo = XmlField('Codigo')
        self.fecha = XmlField('FechaSolicitud')
        self.version = XmlField('Version', value='02')
        super(Cabecera, self).__init__(name, root)


class DatosGeneralesFactura(XmlModel):
    _sort_order = ('datos', 'numero', 'tipo', 'rectificadora', 'fecha', 'cif',
                   'codigo', 'obs', 'importe', 'saldo', 'saldocobro', 'moneda')

    def __init__(self, name, root):
        self.datos = XmlField('DatosGeneralesFactura')
        self.numero = XmlField('NumeroFactura')
        self.tipo = XmlField('TipoFactura')
        self.rectificadora = XmlField('IndicativoFacturaRectificadora')
        self.fecha = XmlField('FechaFactura')
        self.cif = XmlField('CIFEmisora')
        self.codigo = XmlField('CodigoFiscalFactura')
        self.obs = XmlField('Observaciones')
        self.importe = XmlField('Importe')
        self.saldo = XmlField('SaldoFactura')
        self.saldocobro = XmlField('SaldoCobro')
        self.moneda = XmlField('TipoMoneda', value='02')
        super(DatosGeneralesFactura, self).__init__(name, root)


class Periodo(XmlModel):
    _sort_order = ('periodo', 'fecha_desde', 'fecha_hasta', 'meses')

    def __init__(self, name, root):
        self.periodo = XmlField('Periodo')
        self.fecha_desde = XmlField('FechaDesdeFactura')
        self.fecha_hasta = XmlField('FechaHastaFactura')
        self.meses = XmlField('NumeroMeses')
        super(Periodo, self).__init__(name, root)


class DatosFacturaATR(XmlModel):
    _sort_order = ('datos', 'tipo', 'boe', 'tarifa', 'imab', 'periodo')

    def __init__(self, name, root):
        self.datos = XmlField('DatosFacturaATR')
        self.tipo = XmlField('TipoFacturacion')
        self.boe = XmlField('FechaBOE')
        self.tarifa = XmlField('CodigoTarifa')
        self.imab = XmlField('IndAltamedidoenBaja')
        self.periodo = Periodo('Periodo', root='periodo')
        super(DatosFacturaATR, self).__init__(name, root)


class DireccionSuministro(XmlModel):
    _sort_order = ('direccion', 'cups', 'municipio', 'dirsuministro')

    def __init__(self, name, root):
        self.direccion = XmlField('DireccionSuministro')
        self.cups = XmlField('CUPS')
        self.municipio = XmlField('Municipio')
        self.dirsuministro = XmlField('DirSuministro')
        super(DireccionSuministro, self).__init__(name, root)

class Cliente(XmlModel):
    _sort_order = ('cliente', 'cifnif', 'identificador')

    def __init__(self, name, root):
        self.cliente = XmlField('Cliente')
        self.cifnif = XmlField('TipoCIFNIF')
        self.identificador = XmlField('Identificador')
        super(Cliente, self).__init__(name, root)

class DatosGeneralesFacturaATR(XmlModel):
    _sort_order = ('datos', 'direccion', 'cliente', 'contrato', 'datosgrles',
                   'datosatr')

    def __init__(self, name, root):
        self.datos = XmlField('DatosGeneralesFacturaATR')
        self.direccion = DireccionSuministro('DireccionSuministro', root='direccion')
        self.cliente = Cliente('Cliente', root='cliente')
        self.contrato = XmlField('Contrato')
        self.datosgrles = DatosGeneralesFactura('DatosGeneralesFactura', root='datos')
        self.datosatr = DatosFacturaATR('DatosFacturaATR', root='datos')
        super(DatosGeneralesFacturaATR, self).__init__(name, root)

class TerminoPotencia(XmlModel):
    _sort_order = ('termino', 'fecha_desde', 'fecha_hasta', 'periodos')

    def __init__(self, name, root):
        self.termino = XmlField('TerminoPotencia')
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.periodos = []
        super(TerminoPotencia, self).__init__(name, root)


class Potencia(XmlModel):
    _sort_order = ('potencia', 'termino', 'icp', 'importe')

    def __init__(self, name, root):
        self.potencia = XmlField('Potencia')
        self.termino = TerminoPotencia('TerminoPotencia', root='termino')
        self.icp = XmlField('PenalizacionNoICP')
        self.importe = XmlField('ImporteTotalTerminoPotencia')
        super(Potencia, self).__init__(name, root)

class FacturaATR(XmlModel):
    _sort_order = ('factura', 'datosatr', 'potencia')

    def __init__(self, name, root):
        self.factura = XmlField('FacturaATR')
        self.datosatr = DatosGeneralesFacturaATR('DatosGeneralesFacturaATR',
                                            root='datos')
        self.potencia = Potencia('Potencia', root='potencia')
        super(FacturaATR, self).__init__(name, root)

class PeriodoPotencia(XmlModel):
    _sort_order = ('periodo', 'contratada', 'maxdemandada', 'afacturar',
                   'precio')

    def __init__(self, name, root):
        self.periodo = XmlField('Periodo')
        self.contratada = XmlField('PotenciaContratada')
        self.maxdemandada = XmlField('PotenciaMaxDemandada')
        self.afacturar = XmlField('PotenciaAFacturar')
        self.precio = XmlField('PrecioPotencia')
        super(PeriodoPotencia, self).__init__(name, root)


class MensajeFacturacion(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'facturas')

    def __init__(self, name, root):
        self.doc_root = None
        self.mensaje = XmlField('MensajeFacturacion', attributes={
                           'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera('Cabecera', root='cabecera')
        self.facturas = XmlField('Facturas')
        super(MensajeFacturacion, self).__init__(name, root)

    def set_agente(self, agente):
        self.mensaje.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()

