# -*- coding: utf-8 -*-
'''
Mòdul per treballar amb les Factures XML. 
Consta de:

* Funcións per treballar amb lectures
* Classe per mapejar una factura
* Classe per mapejar una lectura
* Classe per mapejar un comptador
'''
def calc_consum(lectura_anterior, lectura_actual, rodes):
    '''
    Funció que ens permet sabel el consum mitjançant la lectura anterior
    i la lectura actual. Si la lectura actual és inferior a l'anterior vol
    dir que el comptador ha donat la volta i sap calcular l'increment segons
    el número de rodes.
    :param numeric lectura_anterior: Lectura anterior
    :param numeric lectura_actual: Lectura actual
    :param integer rodes: Número de rodes del comptador
    '''
    giro = 10**rodes
    consum = lectura_actual - lectura_anterior
    if lectura_actual < lectura_anterior:
        consum += giro
    return consum

class Comptador(object):
    '''
    Classe per mapejar un comptador
    '''
    def __init__(self, numero_serie):
        '''
        Creem un comptador nou
        :param numero_serie: Numero de sèrie del comptador
        '''
        self.numero_serie = numero_serie
        self.lectures = []
    
    def append_lectura(self, lectura):
        '''
        Afegim una lectura al comptador
        :param Lectura lectura: Lectura a afegir
        :returns None
        '''
        self.lectures.append(lectura)

class Lectura(object):
    '''
    Classe per guardar les lectures d'una Factura XML (F1)
    '''
    def __init__(self, magnitud, codi_periode, lectura_anterior,
                 data_anterior, lectura_actual, data_actual, rodes, consum,
                 procedencia_anterior=30, procedencia_actual=30):
        self.magnitud = magnitud
        self.codi_periode = codi_periode
        self.lectura_anterior = lectura_anterior
        self.data_anterior = data_anterior
        self.lectura_actual = lectura_actual
        self.data_actual = data_actual
        self.rodes = rodes
        if consum != self._calc_consum():
            raise Exception("Consum no quadre amb lectures")
        self.consum = consum
        self.procedencia_anterior = procedencia_anterior
        self.procedencia_actual = procedencia_actual
        
    def _calc_consum(self):
        '''
        Funció per calcular el consum
        '''
        return calc_consum(self.lectura_anterior, 
                           self.lectura_actual, self.rodes)

class Factura(object):
    '''
    Classe per mapejar una Factura XML (F1)
    '''
    def __init__(self, numero, data_factura, client_nif, emisor_nif):
        '''
        Creem la factura, camps bàsics: Número, NIF Client, data factura,
        NIF Emisor
        :param numero: Número de la factura
        :param date data_factura: Data de la factura
        :param client_nif: NIF del Client
        :param emisor_nif: NIF de l'Emisor
        '''
        self.numero = numero
        self.data = data_factura
        self.client_nif = client_nif
        self.emisor_nif = emisor_nif
        self.comptadors = []
        
    # Funcions per accedir a l'abonat
    def get_cups(self):
        '''
        Funció per obtenir el CUPS d'una factura
        '''
        pass
        
    # Funcions per accedir a les lectures
    def get_lectures_anteriors(self, unitat_mesura):
        '''
        Funció que retorna les lectures anteriors de la factura segons
        la unitat de mesura desitjada
        '''
        pass
    
    def get_lectura_anterior_periode(self, unitat_mesura, periode):
        pass
    
    def get_lectures_actuals(self, unitat_mesura):
        '''
        Funció que retorna les lectures actuals de la factura segons
        la unitat de mesura desitjada
        '''
        pass
    
    def get_lectura_actual_periode(self, unitat_mesura, periode):
        pass
    
    def get_dates_lectures_anteriors(self, unitat_mesura):
        '''
        Funció que retorna les dates de les lectures anteriors de la 
        factura segons la unitat de mesura desitjada
        '''
        pass
    
    def get_data_lectura_anterior_periode(self, unitat_mesura, periode):
        pass
    
    def get_dates_lectures_acutals(self, unitat_mesura):
        '''
        Funció que retorna les dates de les lectures actuals de la 
        factura segons la unitat de mesura desitjada
        '''
        pass
    
    def get_data_lectura_actual_periode(self, unitat_mesura, periode):
        pass
        
    # Funcions per accedir als consums
    def get_consums(self, unitat_mesura):
        '''
        Ens retorna els consums d'una Factura XML segons la unitat de
        mesura.
        '''
        pass
    
    def get_consum_periode(self, unitat_mesura, periode):
        pass
    
    def append_lectures_comptador(self, comptador):
        '''
        Afegim un comptador amb lectures a una factura
        :param Comptador comptador: Comptador a afegir
        :returns None
        '''
        if comptador not in self.comptadors:
            self.comptadors.append(comptador)
