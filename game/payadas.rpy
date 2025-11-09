label payada_manager(musicPlaying=False):
    # inicia musica

    # if not musicPlaying:
    #     # play music payada_intensa volume 0.5 fadein 1.0
    #     play music paya_1_A volume 0.5 fadein 0


    play music paya_1_A volume 0.5 fadein 0.1
    call payada_vega
    queue music paya_1_final volume 0.5 fadein 0 noloop 
    
    
    call payada_payador
    play music fin_payada_intensa volume 0.5 fadein 1.0 noloop
    
    call payada_terminar
    return
 
label payada_vega:
    # --- Construcción del árbol de payadas usando objetos FrasePayada ---
    python:
        # Importar solo la clase FrasePayada y construir nodos manualmente (sin ArbolPayadas)
        from python.payadas.FrasePayada import FrasePayada

        # Crear nodos (niveles: 1..4). Los leaves están en nivel 4.
        estimado = FrasePayada("Cómo le va mi estimado?", ambicion=0, humildad=1)
        cansado = FrasePayada("Lo veo cansado y sucio", ambicion=1, humildad=0)

        tirarse = FrasePayada("Venga a tirarse un rato", ambicion=0, humildad=1)
        banio = FrasePayada("Por que no se pega un baño", ambicion=1, humildad=0)

        yuyos = FrasePayada("A la sombra de los yuyos", ambicion=1, humildad=0)
        pucho1 = FrasePayada("Y después se me fuma un pucho", ambicion=0, humildad=1)

        tufo = FrasePayada("Que me está matando el tufo", ambicion=1, humildad=0)
        pucho2 = FrasePayada("Y después se me fuma un pucho", ambicion=0, humildad=1)

        # Enlazar nodos manualmente (sig_izq / sig_der)
        estimado.sig_izq = cansado

        cansado.sig_izq = tirarse
        cansado.sig_der = banio

        tirarse.sig_izq = yuyos
        tirarse.sig_der = pucho1

        banio.sig_izq = tufo
        banio.sig_der = pucho2

        # Estado local para la ronda de payada
        payadaVega = []                # lista de FrasePayada elegidas (objetos)
        opciones_nodos = [estimado]
        ambicion_total = 0
        humildad_total = 0

    # Haremos exactamente 4 selecciones (4 niveles)
    $ rondas = 4
    $ nivel_actual = 1
    while nivel_actual <= rondas:

        # Mostrar la payada acumulada (texto)
        $ payada_texto = "\n".join([f.MostrarFrase() for f in payadaVega])
        if payada_texto == "":
            $ payada_texto = "..."
        $ san("[payada_texto]", interact=False)

        # Construir menú con las opciones actuales (pueden ser 1 o 2)
        python:
            menu_items = []
            for n in opciones_nodos:
                if n is None:
                    continue
                menu_items.append( (n.MostrarFrase(), n) )
            # Si no hay opciones, terminamos
            if not menu_items:
                chosen = None
            else:
                chosen = renpy.display_menu(menu_items)

        if chosen is None:
            # No hay más opciones: salimos del bucle estableciendo el nivel final
            $ nivel_actual = rondas + 1

        # Registrar elección
        $ payadaVega.append(chosen)
        # $ ambicion_total += chosen.ambicion
        # $ humildad_total += chosen.humildad
        python:
            # Ejemplo: almacenar en variables globales accesibles por Ren'Py
            store.ambicion = getattr(store, 'ambicion', 0) + chosen.ambicion
            store.humildad = getattr(store, 'humildad', 0) + chosen.humildad
        
        # Seleccionar musica segun nivel y encolar para transición suave
        if nivel_actual == 2:
            queue music paya_1_B volume 0.5 
        if nivel_actual == 3:
            queue music paya_1_A volume 0.5 
        if nivel_actual == 4:
            queue music paya_1_B volume 0.5 
            

        # Mostrar la payada actualizada
        $ payada_texto = "\n".join([f.MostrarFrase() for f in payadaVega])
        san "[payada_texto]"
        # Reinicio la lista de texto para que se pueda leer
        if nivel_actual == 4:
            $ payadaVega = []

        # Preparar las opciones del siguiente nivel
        python:
            siguientes = []
            if chosen.sig_izq:
                siguientes.append(chosen.sig_izq)
            if chosen.sig_der:
                siguientes.append(chosen.sig_der)
            opciones_nodos = siguientes

        $ nivel_actual += 1

    # # Al finalizar, podemos enviar los totales a variables globales si es necesario
    # python:
    #     # Ejemplo: almacenar en variables globales accesibles por Ren'Py
    #     store.ambicion = getattr(store, 'ambicion', 0) + ambicion_total
    #     store.humildad = getattr(store, 'humildad', 0) + humildad_total
    return

label payada_payador:
    show rival_payador
        
    with dissolve
    payador "Muy bien, Vega. Ahora es mi turno."
    play music payada_intensa volume 0.5 fadeout 0.5 fadein 0.5
    hide rival_payador
    with dissolve
    show payador_cantando:
        yalign 1.0
        xalign 50
        zoom 0.9
    with dissolve
   
    #show rival_payador at right:
        # 0.8
        #alpha 0.5
        # 4 alpha 1.0
    #with dissolve
    payador  "{cps=17}No por mucho andar {w=0.5}\nCon las manos en los bolsillos {w=0.5}\nVa encontrar uno más plata {w=0.5}\nNi tampoco prestamillo"
    
    # jump fin_payada
    return


label payada_terminar:
    #hide show rival_payador
    show fondo_negro
    with dissolve
    narrator "{color=#F5D627}{size=35}{b}¡Muy bien! ¡Esa fue una ronda de payadas excelente!{/b}{/size}{/color}"
    return