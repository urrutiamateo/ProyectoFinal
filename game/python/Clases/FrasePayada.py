"""Nodo que representa una frase de payadas para usar en Payadas.

Esta clase sirve como nodo manual: tiene referencias a la opción izquierda y
derecha (`sig_izq`, `sig_der`).
"""

# from typing import Optional
# from .FrasePayada import FrasePayada

class FrasePayada:
    frase: str
    humildad: int
    ambicion: int
    nivel: int
    sig_izq = None
    sig_der = None

    def __init__(self, frase: str, ambicion: int = 0, humildad: int = 0):
        self.frase = frase
        self.ambicion = ambicion
        self.humildad = humildad
        self.sig_izq = None
        self.sig_der = None

    def MostrarFrase(self) -> str:
        return self.frase

    def __repr__(self) -> str:
        return f"FrasePayada(frase={self.frase!r}, ambicion={self.ambicion}, humildad={self.humildad})"
    

