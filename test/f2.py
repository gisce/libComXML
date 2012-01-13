# -*- coding: utf-8 -*-

import pdb

from libcomxml.messages import facturacio as f1

mensaje = f1.MensajeFacturacion()
mensaje.set_agente('0474')

cabecera = f1.Cabecera()
cabecera.feed({
    'ree_emisora': '0474',
    'ree_destino': '0474',
    'proceso': 'F1',
    'paso': '01',
    'solicitud': '123456789012',
    'secuencia': '01',
    'codigo': 'ES0310000000133550XV  ',
    'fecha': '2011-05-07T13:01:05',
})

cliente = f1.Cliente()
cliente.feed({
    'identificador': 'B17736752',
    'cifnif': 'CI', 
})

dirsuministro = f1.DireccionSuministro()
dirsuministro.feed({
    'dirsuministro': 'PL MELA MUTERMILCH, 2, 1, 1',
    'cups': 'ES0310000000133550XV  ',
    'municipio': '1234567',
})

datosgrl = f1.DatosGeneralesFactura()
datosgrl.feed({
    'numero': '0000001',
    'tipo': '01',
    'rectificadora': 'N',
    'fecha': '2011-12-20',
    'cif': 'B17736752',
    'codigo': '0000001',
    'obs': '.',
    'importe': 213.45,
    'saldo': 213.45,
    'saldocobro': 213.45,
})

periodo = f1.Periodo()
periodo.feed({
    'fecha_desde': '2011-09-01',
    'fecha_hasta': '2011-09-30',
    'meses': 1,
})

datosatr = f1.DatosFacturaATR()
datosatr.feed({
    'tipo': '1',
    'boe': '2011-01-01',
    'tarifa': '012',
    'imab': 'N',
    'periodo': periodo,
})

ppotencia1 = f1.PeriodoPotencia()
ppotencia1.feed({
    'contratada': 100,
    'maxdemandada': 90,
    'afacturar': 100,
    'precio': 0.002700,
})

ppotencia2 = f1.PeriodoPotencia()
ppotencia2.feed({
    'contratada': 200,
    'maxdemandada': 190,
    'afacturar': 200,
    'precio': 0.002700,
})

#pdb.set_trace()
terminopotencia = f1.TerminoPotencia()
terminopotencia.feed({
    'fecha_desde': '2011-01-01',
    'fecha_hasta': '2011-01-30',
    'periodos': [ppotencia1, ppotencia2],
})
# terminopotencia.build_tree()

potencia = f1.Potencia()
potencia.feed({
    'icp': 'N',
    'importe': 2677.5100,
    'termino': terminopotencia,
})

datosgrlatr = f1.DatosGeneralesFacturaATR()
datosgrlatr.feed({
    'cliente': cliente,
    'direccion': dirsuministro,
    'contrato': '0123456',
    'datosgrles': datosgrl,
    'datosatr': datosatr,
})

periodoactiva = f1.PeriodoEnergiaActiva()
periodoactiva.feed({
    'valor': 123,
    'precio': 0.123456,
})

terminoactiva = f1.TerminoEnergiaActiva()
terminoactiva.feed({
    'fecha_desde': '2011-12-01',
    'fecha_hasta': '2011-12-31',
    'periodos': [periodoactiva]
})

energia = f1.EnergiaActiva()
energia.feed({
    'termino': terminoactiva,
    'importe': 212.23
})

periodoreactiva = f1.PeriodoEnergiaReactiva()
periodoreactiva.feed({
    'valor': 45.12,
    'precio': 0.123456
})

terminoreactiva = f1.TerminoEnergiaReactiva()
terminoreactiva.feed({
    'fecha_desde': '2011-12-01',
    'fecha_hasta': '2011-12-31',
    'periodos': [periodoreactiva],
})

reactiva = f1.EnergiaReactiva()
reactiva.feed({
    'termino': terminoreactiva,
    'importe': 12.34,
})

iese = f1.ImpuestoElectrico()
iese.feed({
    'base': 123.12,
    'coef': 0.4521,
    'percent': 1.3456,
    'importe': 143.12,
})

alquileres = f1.Alquileres()
alquileres.feed({
    'importe': 0.234,
})

iva = f1.IVA()
iva.feed({
    'base': 123.23,
    'porcentaje': 18.0,
    'importe': 140.12,
})

facturaatr = f1.FacturaATR()
facturaatr.feed({
    'datosatr': datosgrlatr,
    'potencia': potencia,
    'energia': energia,
    'reactiva': reactiva,
    'iese': iese,
    'alquileres': alquileres,
    'iva': iva,
})

ccc = f1.CuentaBancaria()
ccc.feed({
    'banco': 1234,
    'sucursal': 1234,
    'digcontrol': 23,
    'cuenta': 1234567890,
})

registrofin = f1.RegistroFin()
registrofin.feed({
    'importe': 123.12,
    'sfacturacion': 123.12,
    'scobro': 123.12,
    'totalrec': 1,
    'tipomoneda': '02',
    'fvalor': '2012-01-20',
    'flimite': '2012-01-20',
    'ccc': ccc,
    'idremesa': '1234',
})

mensaje.feed({
    'cabecera': cabecera,
    'facturas': [facturaatr, registrofin],
})
mensaje.build_tree()

print(mensaje)

