
from .FrasePayada import FrasePayada





class Payadas:
    
    # estimado = "Cómo le va mi estimado?"
    # cansado =  "Lo veo cansado y sucio"
    # tirarse = "Venga a tirarse un rato"
    # yuyos = "A la sombra de los yuyos"

    # banio = "Por que no se pega un baño"
    # tufo = "Que me esta matando el tufo"
    # pucho = "Y después se me fuma un pucho"
    
    estimado:FrasePayada=FrasePayada("Cómo le va mi estimado?",0,1)
    cansado:FrasePayada=FrasePayada("Lo veo cansado y sucio",0,1)
    tirarse:FrasePayada=FrasePayada("Venga a tirarse un rato",0,1)
    yuyos:FrasePayada=FrasePayada("A la sombra de los yuyos",0,1)
    banio:FrasePayada=FrasePayada("Por que no se pega un baño",0,1)
    tufo:FrasePayada=FrasePayada("Que me esta matando el tufo",0,1)
    pucho:FrasePayada=FrasePayada("Y después se me fuma un pucho",0,1)
    
    
 