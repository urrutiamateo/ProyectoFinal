try:
    import renpy  # Solo se carga correctamente dentro del motor Renpy
except ImportError:
    renpy = None


class Personaje:
    
    def __init__(self, nombre: str, personalizado=None):
        self._nombre = nombre
        self._personalizado = personalizado   #instancia de Character
        #self._formato_texto = formato_texto
        #self._ambicion = ambicion
        #self._humildad = humildad
        
        
#encapsulamiento  
#decorador de Python permite definir getters y setters de una manera más elegante, sin necesidad de llamar funciones con paréntesis.
    @property
    def nombre(self):
        return self._nombre
    

    @property
    def personalizado(self):
        return self._personalizado
    
    @personalizado.setter
    def personalizado(self, nuevo_personalizado):    #Permite asignar o cambiar el Character visual.
        self._personalizado = nuevo_personalizado


    def hablar(self, texto:str):
            if renpy and self._personalizado:   #muestra el dialogo usando el character si está definido
                self._personalizado(texto)
            elif renpy:
                renpy.exports.say(self._nombre, texto)
            else:
                print(f"[{self._nombre}] {texto}")  #uso fuera de Renpy



class SantosVega(Personaje):
    
    #Representa al protagonista Santos Vega.
    #hereda de Personaje e implementa su propio estilo de diálogo.
    def __init__(self, personalizado=None, ambicion=0, humildad=0):
        super().__init__("Santos Vega", personalizado)
        self._ambicion = ambicion   #polimorfismo en la subclase SantosVega
        self.humildad = humildad


    def hablar(self, texto: str, interact=True):
        if renpy and self._personalizado:
            self._personalizado(f"{texto}")
        elif renpy:
            renpy.exports.say(self.nombre, f"{texto}",  interact=interact)  #polimorfismo en el método hablar de ésta subclase
        else:
            print(f"[{self.nombre}] {texto}")


class ViejoPulperia(Personaje):

    #Representa al Viejo de la Pulpería.
    #hereda de Personaje e implementa su propio estilo de diálogo.
    def __init__(self, personalizado=None):
        super().__init__("Don Ernesto", personalizado)

    def hablar(self, texto: str):
        if renpy and self._personalizado:  #si corre dentro de renpy y tiene un character asignado
            self._personalizado(f"{texto}")
        elif renpy:     #si corre dentro de renpy pero sin character
            renpy.exports.say(self.nombre, f"{texto}")
        else:     #si se ejecuta fuera del motor imprime el texto en pantalla
            print(f"[{self.nombre}] {texto}")  

