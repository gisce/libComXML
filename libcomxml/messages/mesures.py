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
        self.consumo = XmlField('ConsumoCalculado')
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


class Medidas(XmlModel):
    _sort_order = ('medidas', 'cups', 'aparatos')

    def __init__(self):
        self.medidas = XmlField('Medidas')
        self.cups = XmlField('CodUnificadoPuntoSuministro')
        self.aparatos = []
        super(Medidas, self).__init__('Medidas', 'medidas')


