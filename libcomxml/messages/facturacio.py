# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101
# pylint: disable=C0111

from ..core import XmlModel, XmlField

class Cabecera(XmlModel):
    _sort_order = ('cabecera', 'ree_emisora', 'ree_destino', 'proceso', 'paso',
                   'solicitud', 'secuencia', 'codigo', 'fecha', 'version')

    def __init__(self):
        self.cabecera = XmlField('Cabecera')
        self.ree_emisora = XmlField('CodigoREEEmpresaEmisora')
        self.ree_destino = XmlField('CodigoREEEmpresaDestino')
        self.proceso = XmlField('CodigoDelProceso')
        self.paso = XmlField('CodigoDePaso')
        self.solicitud = XmlField('CodigoDeSolicitud')
        self.secuencia = XmlField('SecuencialDeSolicitud')
        self.codigo = XmlField('Codigo')
        self.fecha = XmlField('FechaSolicitud')
        self.version = XmlField('Version', value='02')
        super(Cabecera, self).__init__('Cabecera', 'cabecera')


class DatosGeneralesFactura(XmlModel):
    _sort_order = ('datos', 'numero', 'tipo', 'rectificadora', 'fecha', 'cif',
                   'codigo', 'obs', 'importe', 'saldo', 'saldocobro', 'moneda')

    def __init__(self):
        self.datos = XmlField('DatosGeneralesFactura')
        self.numero = XmlField('NumeroFactura')
        self.tipo = XmlField('TipoFactura')
        self.rectificadora = XmlField('IndicativoFacturaRectificadora')
        self.fecha = XmlField('FechaFactura')
        self.cif = XmlField('CIFEmisora')
        self.codigo = XmlField('CodigoFiscalFactura')
        self.obs = XmlField('Observaciones')
        self.importe = XmlField('ImporteTotalFactura')
        self.saldo = XmlField('SaldoFactura')
        self.saldocobro = XmlField('SaldoCobro')
        self.moneda = XmlField('TipoMoneda', value='02')
        super(DatosGeneralesFactura, self).__init__('DatosGeneralesFactura',
                                                    'datos')


class Periodo(XmlModel):
    _sort_order = ('periodo', 'fecha_desde', 'fecha_hasta', 'meses')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.fecha_desde = XmlField('FechaDesdeFactura')
        self.fecha_hasta = XmlField('FechaHastaFactura')
        self.meses = XmlField('NumeroMeses')
        super(Periodo, self).__init__('Periodo', 'periodo')


class DatosFacturaATR(XmlModel):
    _sort_order = ('datos', 'tipo', 'boe', 'tarifa', 'imab', 'periodo')

    def __init__(self):
        self.datos = XmlField('DatosFacturaATR')
        self.tipo = XmlField('TipoFacturacion')
        self.boe = XmlField('FechaBOE')
        self.tarifa = XmlField('CodigoTarifa')
        self.imab = XmlField('IndAltamedidoenBaja')
        self.periodo = Periodo()
        super(DatosFacturaATR, self).__init__('DatosFacturaATR', 'datos')


class DireccionSuministro(XmlModel):
    _sort_order = ('direccion', 'cups', 'municipio', 'dirsuministro')

    def __init__(self):
        self.direccion = XmlField('DireccionSuministro')
        self.cups = XmlField('CUPS')
        self.municipio = XmlField('Municipio')
        self.dirsuministro = XmlField('DirSuministro')
        super(DireccionSuministro, self).__init__('DireccionSuministro',
                                                  'direccion')

class Cliente(XmlModel):
    _sort_order = ('cliente', 'cifnif', 'identificador')

    def __init__(self):
        self.cliente = XmlField('Cliente')
        self.cifnif = XmlField('TipoCIFNIF')
        self.identificador = XmlField('Identificador')
        super(Cliente, self).__init__('Cliente', 'cliente')

class DatosGeneralesFacturaATR(XmlModel):
    _sort_order = ('datos', 'direccion', 'cliente', 'contrato', 'datosgrles',
                   'datosatr')

    def __init__(self):
        self.datos = XmlField('DatosGeneralesFacturaATR')
        self.direccion = DireccionSuministro()
        self.cliente = Cliente()
        self.contrato = XmlField('Contrato')
        self.datosgrles = DatosGeneralesFactura()
        self.datosatr = DatosFacturaATR()
        super(DatosGeneralesFacturaATR,
              self).__init__('DatosGeneralesFacturaATR', 'datos')

class TerminoPotencia(XmlModel):
    _sort_order = ('termino', 'fecha_desde', 'fecha_hasta', 'periodos')

    def __init__(self):
        self.termino = XmlField('TerminoPotencia')
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.periodos = []
        super(TerminoPotencia, self).__init__('TerminoPotencia', 'termino')

# TODO Migrate 'termino's to a list

class Potencia(XmlModel):
    _sort_order = ('potencia', 'termino', 'icp', 'importe')

    def __init__(self):
        self.potencia = XmlField('Potencia')
        self.termino = TerminoPotencia()
        self.icp = XmlField('PenalizacionNoICP')
        self.importe = XmlField('ImporteTotalTerminoPotencia')
        super(Potencia, self).__init__('Potencia', 'potencia')

class ExcesoPotencia(XmlModel):
    _sort_order = ('exceso', 'periodos', 'importe')

    def __init__(self):
        self.exceso = XmlField('ExcesoPotencia')
        self.periodos = []
        self.importe = XmlField('ImporteTotalExcesos')
        super(ExcesoPotencia, self).__init__('ExcesoPotencia', 'exceso')


class TerminoEnergiaActiva(XmlModel):
    _sort_order = ('termino', 'fecha_desde', 'fecha_hasta', 'periodos')

    def __init__(self):
        self.termino = XmlField('TerminoEnergiaActiva')
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.periodos = []
        super(TerminoEnergiaActiva, self).__init__(
            'TerminoEnergiaActiva', 'termino')


class EnergiaActiva(XmlModel):
    _sort_order = ('activa', 'termino', 'importe')

    def __init__(self):
        self.activa = XmlField('EnergiaActiva')
        self.termino = TerminoEnergiaActiva()
        self.importe = XmlField('ImporteTotalEnergiaActiva')
        super(EnergiaActiva, self).__init__('EnergiaActiva', 'activa')


class TerminoEnergiaReactiva(XmlModel):
    _sort_order = ('termino', 'fecha_desde', 'fecha_hasta', 'periodos')

    def __init__(self):
        self.termino = XmlField('TerminoEnergiaReactiva')
        self.fecha_desde = XmlField('FechaDesde')
        self.fecha_hasta = XmlField('FechaHasta')
        self.periodos = []
        super(TerminoEnergiaReactiva, self).__init__(
            'TerminoEnergiaReactiva', 'termino')


class EnergiaReactiva(XmlModel):
    _sort_order = ('reactiva', 'termino', 'importe')

    def __init__(self):
        self.reactiva = XmlField('EnergiaReactiva')
        self.termino = TerminoEnergiaActiva()
        self.importe = XmlField('ImporteTotalEnergiaReactiva')
        super(EnergiaReactiva, self).__init__('EnergiaRectiva', 'reactiva')


class FacturaATR(XmlModel):
    _sort_order = ('factura', 'datosatr', 'potencia', 'energia', 'reactiva')

    def __init__(self):
        self.factura = XmlField('FacturaATR')
        self.datosatr = DatosGeneralesFacturaATR()
        self.potencia = Potencia()
        self.energia = EnergiaActiva()
        self.reactiva = EnergiaReactiva()
        super(FacturaATR, self).__init__('FacturaATR', 'factura')


class PeriodoPotencia(XmlModel):
    _sort_order = ('periodo', 'contratada', 'maxdemandada', 'afacturar',
                   'precio')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.contratada = XmlField('PotenciaContratada')
        self.maxdemandada = XmlField('PotenciaMaxDemandada')
        self.afacturar = XmlField('PotenciaAFacturar')
        self.precio = XmlField('PrecioPotencia')
        super(PeriodoPotencia, self).__init__('PeriodoPotencia', 'periodo')


class PeriodoEnergiaActiva(XmlModel):
    _sort_order = ('periodo', 'valor', 'precio')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor = XmlField('ValorEnergiaActiva')
        self.precio = XmlField('PrecioEnergia')
        super(PeriodoEnergiaActiva, self).__init__('PeriodoEnergiaActiva',
                                                   'periodo')


class PeriodoEnergiaReactiva(XmlModel):
    _sort_order = ('periodo', 'valor', 'precio')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor = XmlField('ValorEnergiaReactiva')
        self.precio = XmlField('PrecioEnergiaReactiva')
        super(PeriodoEnergiaReactiva, self).__init__('PeriodoEnergiaReactiva',
                                                     'periodo')


class ImpuestoElectrico(XmlModel):
    _sort_order = ('iese', 'base', 'coef', 'percent', 'importe')

    def __init__(self):
        self.iese = XmlField('ImpuestoElectrico')
        self.base = XmlField('BaseImponible')
        self.coef = XmlField('Coeficiente')
        self.percent = XmlField('Porcentaje')
        self.importe = XmlField('Importe')
        super(ImpuestoElectrico, self).__init__('ImpuestoElectrico', 'iese')


class Alquileres(XmlModel):
    _sort_order = ('alquileres', 'importe')

    def __init__(self):
        self.alquileres = XmlField('Alquileres')
        self.importe = XmlField('ImporteFacturacionAlquileres')
        super(Alquileres, self).__init__('Alquileres', 'alquileres')


class MensajeFacturacion(XmlModel):
    _sort_order = ('mensaje', 'cabecera', 'facturas')

    def __init__(self):
        self.doc_root = None
        self.mensaje = XmlField('MensajeFacturacion', attributes={
                           'xmlns': 'http://localhost/elegibilidad'})
        self.cabecera = Cabecera()
        self.facturas = XmlField('Facturas')
        super(MensajeFacturacion, self).__init__('MensajeFacturacion',
                                                 'mensaje')

    def set_agente(self, agente):
        self.mensaje.attributes.update({'AgenteSolicitante': agente})
        self.doc_root = self.root.element()

