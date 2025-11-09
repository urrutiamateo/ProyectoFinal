label payada_final_bueno_ebrio_manager(musicPlaying=False):
    # inicia musica

    # if not musicPlaying:
    #     # play music payada_intensa volume 0.5 fadein 1.0
    #     play music paya_1_A volume 0.5 fadein 0


    # play music paya_1_A volume 0.5 fadein 0.1
    
    
    
    call payada_final_bueno_payador_ebrio
    queue music fin_payada_intensa volume 0.5 fadein 1.0 noloop

    
    call payada_final_bueno_vega_ebrio
    queue music paya_1_final volume 0.5 fadein 0 noloop 
    
    call payada_final_bueno_terminar_ebrio
    return
 
label payada_final_bueno_vega_ebrio:
    play music paya_1_A volume 0.5 fadein 0.1
    hide santos_con_cania
    with dissolve
    show santos_payando at left
    with dissolve
    # --- Construcción del árbol de payadas usando objetos FrasePayada ---
    python:
        # Importar solo la clase FrasePayada y construir nodos manualmente (sin ArbolPayadas)
        from python.payadas.FrasePayada import FrasePayada

        # Crear nodos (niveles: 1..4). Los leaves están en nivel 4.
        verso1 = FrasePayada("Anduve sí, por lo oscuro,", ambicion=0, humildad=1)
        verso2 = FrasePayada("y el humo me dio su abrazo,", ambicion=1, humildad=0)

        verso3 = FrasePayada("mas si el diablo me invitó al truco,", ambicion=0, humildad=1)
        verso4 = FrasePayada("yo le gané con un cuatro.", ambicion=1, humildad=0)

        verso5 = FrasePayada("Cavé, sí, pa’ ver si hallaba,", ambicion=1, humildad=0)
        verso6 = FrasePayada("algún cobre pa’ mi pena,", ambicion=0, humildad=1)

        verso7 = FrasePayada("Pero ahora brindo con vino,", ambicion=1, humildad=0)
        verso8 = FrasePayada("¡que es mejor trato divino!", ambicion=0, humildad=1)

        

        # Enlazar nodos manualmente (sig_izq / sig_der)
        
        verso1.sig_izq = verso2
        verso2.sig_izq = verso3
        verso3.sig_izq = verso4
        verso4.sig_izq = verso5
        verso5.sig_izq = verso6
        verso6.sig_izq = verso7
        verso7.sig_izq = verso8

       


        # Estado local para la ronda de payada
        payadaVega = []                # lista de FrasePayada elegidas (objetos)
        opciones_nodos = [verso1,verso5]
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
        if nivel_actual == 5:
            queue music paya_1_A volume 0.5 
        if nivel_actual == 6:
            queue music paya_1_B volume 0.5 
        if nivel_actual == 7:
            queue music paya_1_A volume 0.5 
        if nivel_actual == 8:
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

label payada_final_bueno_payador_ebrio:
    show rival_payador at right:
        ypos 1.1
        
    with dissolve
    payador "Muy bien, Vega. Es buen momento para una payada."
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
    payador  "{cps=17}¡Mire quién vuelve del monte!{w=0.5}\nCon el sombrero chamuscao, {w=0.5}\nparece que allá en el fondo {w=0.5}\nel fuego lo ha acariciao."

    
    
    # jump fin_payada
    return


label payada_final_bueno_terminar_ebrio:
    #hide show rival_payador
    #stop music fadeout 2.0
    show fondo_negro
    with dissolve
    play sound aplausos volume 0.7 fadein 0.5
    narrator "Y esa noche, entre amigos, risas, el vino y la guitarra, Santos entendió su destino.{w}No necesitaba fama ni gloria. Su canto ya era eterno… porque nacía de su alma libre."
    return