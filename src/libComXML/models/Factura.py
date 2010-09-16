# -*- coding: utf-8 -*-
class Factura:
    
    def __init__(self):
        nif_client = None
        contracte = None
        numero = None
        tipus = None
        rectificadora = None
        data_factura = None
        pass
        
    # Funcions per accedir a l'abonat
    def get_cups(self):
        return self.factura.DatosGeneralesFacturaATR
    
    # Funcions per accedir a les lectures
    def get_lectures_anteriors(self, um):
        pass
    
    def get_lectura_anterior_periode(self, um, periode):
        pass
    
    def get_lectures_actuals(self, um):
        pass
    
    def get_lectura_actual_periode(self, um, periode):
        pass
    
    def get_dates_lectures_anteriors(self, um):
        pass
    
    def get_data_lectura_anterior_periode(self, um, periode):
        pass
    
    def get_dates_lectures_acutals(self, um):
        pass
    
    def get_data_lectura_actual_periode(self, um, periode):
        pass
        
    # Funcions per accedir als consums
    def get_consums(self, um):
        pass
    
    def get_consum_periode(self, um, periode):
        pass