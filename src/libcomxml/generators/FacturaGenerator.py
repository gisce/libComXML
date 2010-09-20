# -*- coding: utf-8 -*-
from libcomxml.bindings import Facturacion
from libcomxml.models.Factura import Factura

class FacturaGenerator(object):
    
    def __init__(self):
        self.binding = None
        self.factures = []
    
    def generate_from_binding(self, binding):
        '''
        Genera les factures a través d'un binding passat com a paràmetre.
        Aquesta funció comprovarà que el binding és del tipus _Facturacion_
        '''
        if not isinstance(binding, Facturacion):
            raise Exception("This binding is not supported")
        self.binding = binding
        self._generate_factures()
        return self.factures
    
    def generate_from_xml(self, xml_text):
        '''
        Genera les factures a través d'un XML i creant un binding per aquest
        XML.
        '''
        self.binding = Facturacion.CreateFromDocument(xml_text)
        self._generate_factures()
        return self.factures
    
    def _generate_termes(self, termes, claus_valors):
        '''
        Generem un diccionari per tenir les línies de factura que forme
        el termes que es passin per paràmetre. Segons el diccionari
        claus_valors, assignarem a la clau 'x' l'atribut 'y' del terme.
        '''
        res_termes = {}
        periode = 1
        for terme in termes:
            nom_periode = 'P%i' % periode
            res_termes[nom_periode] = {}
            for key,value in claus_valors.items():
                res_termes[nom_periode][key] = getattr(terme, value)
            periode += 1
        return res_termes
    
    def _generate_termes_energia_activa(self, termes):
        '''
        Generem els termes d'energia activa
        '''
        claus_valors = {'valor': 'ValorEnergiaActiva', 'preu': 'PrecioEnergia'}
        return self._generate_termes(termes, claus_valors)
    
    def _generate_termes_energia_reactiva(self, termes):
        '''
        Generem els termes d'energia reactiva
        '''
        claus_valors = {'valor': 'ValorEnergiaReactiva', 
                        'preu': 'PrecioEnergiaReactiva'}
        return self._generate_termes(termes, claus_valors)
    
    def _generate_termes_potencia(self, termes):
        '''
        Generem els termes de potència
        '''
        claus_valors = {
                    'contractada': 'PotenciaContratada',
                    'demandada': 'PotenciaMaxDemandada',
                    'facturar': 'PotenciaAFacturar',
                    'preu': 'PrecioPotencia'
        }
        return self._generate_termes(termes, claus_valors)

    def _generate_factures(self):
        '''
        Funció interna per generar les factures
        '''
        for f in self.binding.Facturas.FacturaATR:
            
            client_nif = f.DatosGeneralesFacturaATR.Cliente.Identificador
            # Fem un mapping la variable dg apunta a DatosGeneralesFactura
            dgf = f.DatosGeneralesFacturaATR.DatosGeneralesFactura
            numero_factura = dgf.NumeroFactura
            data_factura = dgf.FechaFactura
            emisor_nif = dgf.DatosCIFEmisora
            factura = Factura(numero_factura, data_factura, client_nif, emisor_nif)
            
            factura.contracte = f.DatosGeneralesFacturaATR.Contrato
            factura.tipus = dgf.TipoFactura
            factura.rectificativa = dgf.IndicativoFacturaRectificadora
            factura.import_total = dgf.ImporteTotalFactura
            factura.saldo_factura = dgf.SaldoFactura
            factura.saldo_cobro = dgf.SaldoCobro
            factura.mondeda = dgf.TipoMoneda
            # Mapping DatosFacturaATR
            dfa = f.DatosGeneralesFacturaATR.DatosFacturaATR
            factura.tipus_facturacio = dfa.TipoFacturacion
            factura.data_boe = dfa.FechaBOE
            factura.codi_tarifa = dfa.CodigoTarifa
            factura.medida_en_baja = dfa.IndAltamedidoenBaja
            factura.inici_periode = dfa.Periodo.FechaDesdeFactura
            factura.final_periode = dfa.Periodo.FechaHastaFactura
            factura.numero_mesos = dfa.Periodo.NumeroMeses
            # Mapping TerminoPotencia
            tp = f.Potencia.TerminoPotencia
            f.potencia_data_inici = tp.FechaDesde
            f.potencia_data_final = tp.FechaHasta
            factura.potencies_contactades = self._generate_termes_potencia(tp.Periodo)
            factura.import_total_potencia = f.Potencia.ImporteTotalTerminoPotencia
            factura.penalitzacio_no_icp = f.Potencia.PenalizacionNoICP
            # Mapping TerminoEnergiaActiva
            tea = f.EnergiaActiva.TerminoEnergiaActiva
            factura.energia_activa_data_inici = tea.FechaDesde
            factura.energia_activa_data_final = tea.FechaHasta
            # Generem els termes d'energia activa
            factura.termes_energia_activa = self._generate_termes_energia_activa(tea.Periodo)
            factura.import_total_energia_activa = f.EnergiaActiva.ImporteTotalEnergiaActiva
            # Mapping TerminoEnergiaReactiva
            ter = f.EnergiaReactiva.TerminoEnergiaReactiva
            factura.energia_reactiva_data_inici = ter.FechaDesde
            factura.energia_reactiva_data_final = ter.FechaHasta
            factura.termes_energia_reactiva = self._generate_termes_energia_reactiva(ter.Periodo)
            
            # Mapping ImpuestoElectrico
            ie = f.ImpuestoElectrico
            factura.impost_electric_base = ie.BaseImponible
            factura.impost_electric_cof = ie.Coeficiente
            factura.impost_electric_percentatge = ie.Porcentaje
            factura.impost_electric_import = ie.Importe
            # Alquileres
            factura.import_alquileres = f.Alquileres.ImporteFacturacionAlquileres
            # IVA
            factura.iva_base_imponible = f.IVA.BaseImponible
            factura.iva_percentatge = f.IVA.Porcentaje
            factura.iva_import = f.IVA.Importe
            
        self.factures.append(factura)
