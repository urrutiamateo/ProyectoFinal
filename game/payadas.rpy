label payada_manager(musicPlaying=False):
    # inicia musica

    if not musicPlaying:
        play music payada_intensa volume 0.5 fadein 1.0
     
    call payada_vega
    call payada_payador
    play music fin_payada_intensa volume 0.5 fadein 1.0
    call payada_terminar
    return



label payada_vega:

    # Lista de frases
    $ estimado = "Cómo le va mi estimado?"
    $ cansado =  "Lo veo cansado y sucio"
    $ tirarse = "Venga a tirarse un rato"
    $ yuyos = "A la sombra de los yuyos"

    $ banio = "Por que no se pega un baño"
    $ tufo = "Que me esta matando el tufo"
    $ pucho = "Y después se me fuma un pucho"

    # Lista donde se arma la payada
    $ payadaVega = []
    # Lista de opciones completa
    $ opciones = []
    # default rondas = 4

    #funciones python
    python:
        # Función para actualizar la payada
        def actualizar_payada(eleccion):
            if eleccion not in payadaVega:
                payadaVega.append(eleccion)
            return
        
        # Función para obtener la payada como una cadena
        def obtener_payada():
            payada_texto = ""
            for linea in payadaVega:
                payada_texto += linea + "\n"
            return payada_texto.strip()

        def actualizar_opciones(eleccion) -> list:
            opciones = []
            if eleccion == estimado:
                opciones = [cansado]
            elif eleccion == cansado:
                opciones = [tirarse, banio]
            elif eleccion == tirarse:
                opciones = [yuyos, pucho]
            elif eleccion == banio:
                opciones = [tufo, pucho]
            elif eleccion == yuyos:
                #sumamos a la variable humildad
                global humildad
                humildad += 5
            elif eleccion == tufo:
                #sumamos a la variable ambicion
                global ambicion
                ambicion += 5
            else:
                opciones = [estimado, cansado, tirarse, yuyos, pucho, banio, tufo]
            return opciones

    
    $ opciones = [estimado]
    while len(payadaVega) < 4:  # Mientras no se hayan completado 5 líneas
        $ payada_actual = obtener_payada()  # Obtiene la payada actualizada.
        $ san("[payada_actual]",interact=False) # Muestra la payada actualizada.
        $ eleccion = renpy.display_menu([(opcion, opcion) for opcion in opciones])
        $ actualizar_payada(eleccion)  # Actualiza la payada con la opción seleccionada.
        $ payada_actual = obtener_payada()  # Obtiene la payada actualizada.
        san "[payada_actual]" # Muestra la payada actualizada.
        $ opciones = actualizar_opciones(eleccion)
        
    return

label payada_payador:
    payador "Muy bien, Vega. Ahora es mi turno."
    # Aquí puedes añadir la lógica para la payada del Payador.
    show rival_payador at right:
        zoom 0.8
        alpha 0.5
        linear 4 alpha 1.0
    with dissolve
    payador  "No por mucho andar {w=0.5} \n
            Con las manos en los bolsillos {w=0.5} \n
            Va encontrar uno más plata {w=0.5}\n
            Ni tampoco prestamillo"
    
    # jump fin_payada
    
    return


label payada_terminar:
    hide show rival_payador
    narrator "¡Muy bien! ¡Esa fue una ronda de payadas excelente!"
    return