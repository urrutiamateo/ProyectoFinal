"""Nodo que representa una frase dentro del árbol de payadas.

Esta clase sirve como nodo manual: tiene referencias a la opción izquierda y
derecha (`sig_izq`, `sig_der`) y un nivel opcional para facilitar búsquedas
por nivel desde `ArbolPayadas`.
"""

from typing import Optional


class FrasePayada:
    frase: str
    humildad: int
    ambicion: int
    nivel: int
    sig_izq: Optional['FrasePayada']
    sig_der: Optional['FrasePayada']

    def __init__(self, frase: str, ambicion: int = 0, humildad: int = 0, nivel: int = 1):
        self.frase = frase
        self.ambicion = ambicion
        self.humildad = humildad
        self.nivel = nivel
        self.sig_izq = None
        self.sig_der = None

    def MostrarFrase(self) -> str:
        return self.frase

    def __repr__(self) -> str:
        return f"FrasePayada(frase={self.frase!r}, nivel={self.nivel}, ambicion={self.ambicion}, humildad={self.humildad})"
    

