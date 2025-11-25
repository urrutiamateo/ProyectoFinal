


from abc import ABC, abstractmethod



class Payada:
    
    frase_armada :str = []
    cant_rondas :int = 4
    opciones_nodos = []


    
    _nivel_actual=1
    
    def __init__(self, rondas:int=4):
        self.cant_rondas = rondas
        pass
    
    def Mostrar_Payada(self):
        pass
    
    
 