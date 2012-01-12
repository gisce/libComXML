# -*- coding: utf-8 -*-

# pylint: disable=E1002
# pylint: disable=E1101

from ..core import XmlModel, XmlField

class LecturaDesde(XmlModel):
    _sort_order = ('desde', 'fechahora', 'procedencia', 'lectura')

    def __init__(self):
        self.desde = XmlField('LecturaDesde')
        self.fechahora = XmlField('FechaHora')
        self.procedencia = XmlField('Procedencia')
        self.lectura = XmlField('Lectura')
        super(LecturaDesde, self).__init__('LecturaDesde', 'desde')


class LecturaHasta(XmlModel):
    _sort_order = ('hasta', 'fechahora', 'procedencia', 'lectura')

    def __init__(self):
        self.hasta = XmlField('LecturaHasta')
        self.fechahora = XmlField('FechaHora')
        self.procedencia = XmlField('Procedencia')
        self.lectura = XmlField('Lectura')
        super(LecturaHasta, self).__init__('LecturaHasta', 'hasta')


class Integrador(XmlModel):
    _sort_order = ('integrador', 'magnitud', 'codperiodo', 'multi', 'enteras',
                   'decimales', 'consumo', 'desde', 'hasta')

    def __init__(self):
        self.integrador = XmlField('Integrador')
        self.magnitud = XmlField('Magnitud')
        self.codperiodo = XmlField('CodigoPeriodo')
        self.multi = XmlField('ConstanteMultiplicadora')
        self.enteras = XmlField('NumeroRuedasEnteras')
        self.decimales = XmlField('NumeroRuedasDecimales')
        self.desde = LecturaDesde()
        self.hasta = LecturaHasta()
        super(Integrador, self).__init__('Integrador', 'integrador')


class Aparato(XmlModel):
    _sort_order = ('aparato', 'tipo', 'marca', 'numserie', 'codigodh',
                   'integradores')

    def __init__(self):
        self.aparato = XmlField('Aparato')
        self.tipo = XmlField('Tipo')
        self.marca = XmlField('Marca')
        self.numserie = XmlField('NumeroSerie')
        self.codigodh = XmlField('CodigoDH')
        self.integradores = []
        super(Aparato, self).__init__('Aparato', 'aparato')


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
        self.importe = XmlField('ImporteTotal')
        self.sfacturacion = XmlField('SaldoTotalFacturacion')
        self.scobro = XmlField('SaldoTotalCobro')
        self.totalrec = XmlField('TotalRecibos')
        self.tipomoneda = XmlField('TipoMoneda')
        self.fvalor = XmlField('FechaValor')
        self.flimite = XmlField('FechaLimitePago')
        self.ccc = CuentaBancaria()
        self.idremesa = XmlField('IdRemesa')
        super(RegistroFin, self).__init__('RegistroFin', 'registro')


class Medidas(XmlModel):
    _sort_order = ('medidas', 'cups', 'aparatos')

    def __init__(self):
        self.medidas = XmlField('Medidas')
        self.cups = XmlField('CodUnificadoPuntoSuministro')
        self.aparatos = []
        super(Medidas, self).__init__('Medidas', 'medidas')


