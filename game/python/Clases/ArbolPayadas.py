from .FrasePayada import FrasePayada
from typing import Optional, Tuple, List


class ArbolPayadas:
    NIVEL_INICIO = 1
    NIVEL_ESTIMADO = 2
    NIVEL_CANSADO = 3
    NIVEL_TIRASTE_BARRIO = 4
    NIVEL_FINAL = 5
    
    def __init__(self):
        self.raiz = None
        self.nivel_actual: int = self.NIVEL_INICIO
        self.altura: int = 5
    
    def actualizar_payada(self, frase_payada: FrasePayada) -> None:
        """
        Actualiza la lista de frases que serán la payada completa que se muestra al ir 
        avanzando en el árbol
        """
        if not self.raiz:
            self.raiz = frase_payada
        self.nivel_actual = frase_payada.nivel
    
    def actualizar_opciones(self, nodo_actual: FrasePayada) -> Tuple[Optional[FrasePayada], Optional[FrasePayada]]:
        """
        Devuelve las frases de los nodos siguientes que se van a mostrar al jugador 
        para que elija
        """
        return (nodo_actual.sig_izq, nodo_actual.sig_der)
    
    def actualizar_nivel(self) -> int:
        """
        Devuelve el valor del nivel actual para actualizar la música del juego (efecto épico)
        """
        return self.nivel_actual
    
    def actualizar_valores(self, frase_elegida: FrasePayada) -> Tuple[int, int]:
        """
        Suma los valores de humildad/ambición al repositorio global
        """
        return (frase_elegida.humildad, frase_elegida.ambicion)
    
    def obtener_raiz(self) -> Optional[FrasePayada]:
        """
        Retorna la frase raíz del árbol
        """
        return self.raiz
    
    def obtener_nodo_actual(self) -> Optional[FrasePayada]:
        """
        Retorna el nodo actual según el nivel
        """
        if self.esta_vacio():
            return None
        return self._obtener_nodo_nivel(self.raiz, self.nivel_actual)
    
    def _obtener_nodo_nivel(self, nodo: Optional[FrasePayada], nivel: int) -> Optional[FrasePayada]:
        """
        Método auxiliar para obtener un nodo en un nivel específico
        """
        if not nodo or nodo.nivel > nivel:
            return None
        
        if nodo.nivel == nivel:
            return nodo
            
        # Buscar en ambas ramas
        izq = self._obtener_nodo_nivel(nodo.sig_izq, nivel)
        if izq:
            return izq
            
        return self._obtener_nodo_nivel(nodo.sig_der, nivel)
    
    def recorrer_nivel(self, nivel: int) -> List[FrasePayada]:
        """
        Recorre el árbol por nivel y devuelve todas las frases en ese nivel
        """
        if not self.raiz or nivel < 1 or nivel > self.altura:
            return []
        
        resultado = []
        self._recorrer_nivel_recursivo(self.raiz, nivel, 1, resultado)
        return resultado
    
    def _recorrer_nivel_recursivo(self, nodo: Optional[FrasePayada], nivel_objetivo: int, 
                                nivel_actual: int, resultado: list) -> None:
        """
        Método auxiliar para recorrer el árbol por nivel
        """
        if not nodo:
            return
        
        if nivel_actual == nivel_objetivo:
            resultado.append(nodo)
            return
        
        if nivel_actual < nivel_objetivo:
            self._recorrer_nivel_recursivo(nodo.sig_izq, nivel_objetivo, nivel_actual + 1, resultado)
            self._recorrer_nivel_recursivo(nodo.sig_der, nivel_objetivo, nivel_actual + 1, resultado)
    
    def esta_vacio(self) -> bool:
        """
        Verifica si el árbol está vacío
        """
        return self.raiz is None