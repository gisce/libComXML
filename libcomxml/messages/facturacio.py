# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101
# pylint: disable=C0111

from ..core import XmlModel, XmlField
import libcomxml.messages.mesures as m

class Cabecera(XmlModel):
    _sort_order = ('cabecera', 'ree_emisora', 'ree_destino', 'proceso', 'paso',
                   'solicitud', 'secuencia', 'codigo', 'fecha', 'version')

    def rep_solicitud(self, codsol):
        codsol = ''.join([x for x in codsol if x.isalnum()])
        return codsol.ljust(12, '0')[:12]

    def __init__(self):
        self.cabecera = XmlField('Cabecera')
        self.ree_emisora = XmlField('CodigoREEEmpresaEmisora')
        self.ree_destino = XmlField('CodigoREEEmpresaDestino')
        self.proceso = XmlField('CodigoDelProceso')
        self.paso = XmlField('CodigoDePaso')
        self.solicitud = XmlField('CodigoDeSolicitud', rep=self.rep_solicitud)
        self.secuencia = XmlField('SecuencialDeSolicitud')
        self.codigo = XmlField('Codigo', rep=lambda x: x.ljust(22, '0'))
        self.fecha = XmlField('FechaSolicitud', rep=lambda x: '%sT00:00:00' % x)
        self.version = XmlField('Version', value='02')
        super(Cabecera, self).__init__('Cabecera', 'cabecera')


class DatosGeneralesFactura(XmlModel):
    _sort_order = ('datos', 'numero', 'tipo', 'rectificadora', 'ref', 'fecha',
                   'cif', 'codigo', 'obs', 'importe', 'saldo', 'saldocobro',
                   'moneda')

    def __init__(self):
        self.datos = XmlField('DatosGeneralesFactura')
        self.numero = XmlField('NumeroFactura', rep=lambda x: x[:26])
        self.tipo = XmlField('TipoFactura')
        self.rectificadora = XmlField('IndicativoFacturaRectificadora')
        self.ref = XmlField('NumeroFacturaRectificada')
        self.fecha = XmlField('FechaFactura')
        self.cif = XmlField('CIFEmisora')
        self.codigo = XmlField('CodigoFiscalFactura', rep=lambda x: x[:17])
        self.obs = XmlField('Observaciones')
        self.importe = XmlField('ImporteTotalFactura', rep=lambda x: '%.2f' % x)
        self.saldo = XmlField('SaldoFactura', rep=lambda x: '%.2f' % x)
        self.saldocobro = XmlField('SaldoCobro', rep=lambda x: '%.2f' % x)
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
        self.cups = XmlField('CUPS', rep=lambda x: x.ljust(22, ' '))
        self.municipio = XmlField('Municipio')
        self.dirsuministro = XmlField('DirSuministro', rep=lambda x: x[:60])
        super(DireccionSuministro, self).__init__('DireccionSuministro',
                                                  'direccion')

class Cliente(XmlModel):
    _sort_order = ('cliente', 'cifnif', 'identificador')

    def __init__(self):
        self.cliente = XmlField('Cliente')
        self.cifnif = XmlField('TipoCIFNIF')
        self.identificador = XmlField('Identificador', rep=lambda x: x[2:])
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


class Potencia(XmlModel):
    _sort_order = ('potencia', 'termino', 'icp', 'importe')

    def __init__(self):
        self.potencia = XmlField('Potencia')
        self.termino = []
        self.icp = XmlField('PenalizacionNoICP')
        self.importe = XmlField('ImporteTotalTerminoPotencia',
                                rep=lambda x: '%.2f' % x)
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
        self.termino = []
        self.importe = XmlField('ImporteTotalEnergiaActiva',
                                rep=lambda x: '%.2f' % x)
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
        self.termino = []
        self.importe = XmlField('ImporteTotalEnergiaReactiva',
                                rep=lambda x: '%.2f' % (x or bool(x)))
        super(EnergiaReactiva, self).__init__('EnergiaRectiva', 'reactiva')


class PeriodoPotencia(XmlModel):
    _sort_order = ('periodo', 'contratada', 'maxdemandada', 'afacturar',
                   'precio')

    def _pot_rep(self, val):
        return ('%.0f' % val)[:11]

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.contratada = XmlField('PotenciaContratada', rep=self._pot_rep)
        self.maxdemandada = XmlField('PotenciaMaxDemandada', rep=self._pot_rep)
        self.afacturar = XmlField('PotenciaAFacturar', rep=self._pot_rep)
        self.precio = XmlField('PrecioPotencia', rep=lambda x: '%.8f' % x)
        super(PeriodoPotencia, self).__init__('PeriodoPotencia', 'periodo')


class PeriodoEnergiaActiva(XmlModel):
    _sort_order = ('periodo', 'valor', 'precio')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor = XmlField('ValorEnergiaActiva', rep=lambda x: '%.2f' % x)
        self.precio = XmlField('PrecioEnergia', rep=lambda x: '%.8f' % x)
        super(PeriodoEnergiaActiva, self).__init__('PeriodoEnergiaActiva',
                                                   'periodo')


class PeriodoEnergiaReactiva(XmlModel):
    _sort_order = ('periodo', 'valor', 'precio')

    def __init__(self):
        self.periodo = XmlField('Periodo')
        self.valor = XmlField('ValorEnergiaReactiva', rep=lambda x: '%.2f' % x)
        self.precio = XmlField('PrecioEnergiaReactiva',
                               rep=lambda x: '%.8f' % x)
        super(PeriodoEnergiaReactiva, self).__init__('PeriodoEnergiaReactiva',
                                                     'periodo')


class ImpuestoElectrico(XmlModel):
    _sort_order = ('iese', 'base', 'coef', 'percent', 'importe')

    def __init__(self):
        self.iese = XmlField('ImpuestoElectrico')
        self.base = XmlField('BaseImponible')
        self.coef = XmlField('Coeficiente')
        self.percent = XmlField('Porcentaje')
        self.importe = XmlField('Importe', rep=lambda x: '%.2f' % x)
        super(ImpuestoElectrico, self).__init__('ImpuestoElectrico', 'iese')


class Alquileres(XmlModel):
    _sort_order = ('alquileres', 'importe')

    def __init__(self):
        self.alquileres = XmlField('Alquileres')
        self.importe = XmlField('ImporteFacturacionAlquileres',
                                rep=lambda x: '%.2f' % x)
        super(Alquileres, self).__init__('Alquileres', 'alquileres')


class IVA(XmlModel):
    _sort_order = ('iva', 'base', 'porcentaje', 'importe')

    def __init__(self):
        self.iva = XmlField('IVA')
        self.base = XmlField('BaseImponible', rep=lambda x: '%.4f' % x)
        self.porcentaje = XmlField('Porcentaje', rep=lambda x: '%.2f' % x)
        self.importe = XmlField('Importe', rep=lambda x: '%.4f' % x)
        super(IVA, self).__init__('IVA', 'iva')

class Refacturacion(XmlModel):
    _sort_order = ('refacturacion', 'tipo', 'fecha_desde', 'fecha_hasta',
                   'consumo', 'importe_total')
    
    def __init__(self):
        self.refacturacion = XmlField('Refacturacion')
        self.tipo = XmlField('Tipo')
        self.fecha_desde = XmlField('RFechaDesde')
        self.fecha_hasta = XmlField('RFechaHasta')
        self.consumo = XmlField('RConsumo',
                                rep=lambda x: '%.2f' % x)
        self.importe_total = XmlField('ImporteTotal',
                                      rep=lambda x: '%.4f' % x)
        super(Refacturacion, self).__init__('Refacturacion', 'refacturacion')

class FacturaATR(XmlModel):
    _sort_order = ('factura', 'datosatr', 'potencia', 'energia', 'reactiva',
                   'iese', 'alquileres', 'iva', 'refacturaciones', 'medidas')

    def __init__(self):
        self.factura = XmlField('FacturaATR')
        self.datosatr = DatosGeneralesFacturaATR()
        self.potencia = Potencia()
        self.energia = EnergiaActiva()
        self.reactiva = EnergiaReactiva()
        self.iese = ImpuestoElectrico()
        self.alquileres = Alquileres()
        self.iva = IVA()
        self.refacturaciones =  XmlField('Refacturaciones')
        self.medidas = m.Medidas()
        super(FacturaATR, self).__init__('FacturaATR', 'factura')


class CuentaBancaria(XmlModel):
    _sort_order = ('ccc', 'banco', 'sucursal', 'digcontrol', 'cuenta')

    def __init__(self):
        self.ccc = XmlField('CuentaBancaria')
        self.banco = XmlField('Banco')
        self.sucursal = XmlField('Sucursal')
        self.digcontrol = XmlField('DC')
        self.cuenta = XmlField('Cuenta')
        super(CuentaBancaria, self).__init__('CuentaBancaria', 'ccc')


class RegistroFin(XmlModel):
    _sort_order = ('registro', 'importe', 'sfacturacion', 'scobro', 'totalrec',
                   'tipomoneda', 'fvalor', 'flimite', 'ccc', 'idremesa')

    def __init__(self):
        self.registro = XmlField('RegistroFin')
        self.importe = XmlField('ImporteTotal', rep=lambda x: '%.2f' % x)
        self.sfacturacion = XmlField('SaldoTotalFacturacion',
                                     rep=lambda x: '%.2f' % x)
        self.scobro = XmlField('SaldoTotalCobro', rep=lambda x: '%.2f' % x)
        self.totalrec = XmlField('TotalRecibos')
        self.tipomoneda = XmlField('TipoMoneda')
        self.fvalor = XmlField('FechaValor')
        self.flimite = XmlField('FechaLimitePago')
        self.ccc = CuentaBancaria()
        self.idremesa = XmlField('IdRemesa')
        super(RegistroFin, self).__init__('RegistroFin', 'registro')


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

