label payada_final_bueno_ebrio_manager(musicPlaying=False):
    # inicia musica

    # if not musicPlaying:
    #     # play music payada_intensa volume 0.5 fadein 1.0
    #     play music paya_1_A volume 0.5 fadein 0


    # play music paya_1_A volume 0.5 fadein 0.1
    
    
    
    call payada_final_bueno_payador_ebrio from _call_payada_final_bueno_payador_ebrio
    queue music fin_payada_intensa volume 0.5 fadein 1.0 noloop

    
    call payada_final_bueno_vega_ebrio from _call_payada_final_bueno_vega_ebrio
    queue music paya_1_final volume 0.5 fadein 0 noloop 
    
    call payada_final_bueno_terminar_ebrio from _call_payada_final_bueno_terminar_ebrio
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

        #verso1 = FrasePayada("Anduve sí, por lo oscuro,")
        #verso2 = FrasePayada("y el humo me dio su abrazo,")
        #verso3 = FrasePayada("y la sombra fue mi lazo,")

        #verso4 = FrasePayada("mas si el diablo me invitó al truco,")
        #verso5 = FrasePayada("el diablo me hablo despacio,")
        
        #verso6 = FrasePayada("el vino me dio su manto,")
        #verso7 = FrasePayada("la tentación buscó mi rumbo,")

        #verso8 = FrasePayada("yo le gané con un cuatro.")
        #verso9 = FrasePayada("le cante y perdió su paso.")

        #verso10 = FrasePayada("y al mal no le di mi brazo.")
        #verso11 = FrasePayada("y escapé de su regazo.")
        
        #verso12 = FrasePayada("y brindé por su fracaso.")
        #verso13 = FrasePayada("y salí buscando el vaso.")
        
        #verso14 = FrasePayada("pero la esquivé sin fracaso.")
        #verso15 = FrasePayada("y no caí en su abrazo.")
        # --- NIVEL 1 (RAÍZ) ---
        verso1 = FrasePayada("Si canto, canto sin pena,")


        # --- NIVEL 2 (LA ELECCIÓN) ---

        # RAMA IZQUIERDA: Cambié "pa' mi pena" por "en la arena" para no repetir la palabra "pena".
        verso2 = FrasePayada("buscando plata en la arena,")

        # RAMA DERECHA: Cambié "y una bota" por "aunque la bota" para que conecte con el verso 1.
        verso3 = FrasePayada("aunque la bota me aprieta,")


        # --- NIVEL 3 (DESARROLLO) ---

        # RAMA IZQUIERDA (Excavación):
        verso4 = FrasePayada("cavé, sí, pa’ ver si hallaba,")
        verso5 = FrasePayada("pero el suelo estaba duro...")

        # RAMA DERECHA (Surrealista):
        verso6 = FrasePayada("y la luna que me inquieta,")
        verso7 = FrasePayada("y mi caballo me habla,")


        # --- NIVEL 4 (REMATES) ---

        # RAMA IZQUIERDA (Excavación):
        verso8 = FrasePayada("¡y mi pala era una espuela!")
        verso9 = FrasePayada("¡y encontré solo una muela!")

        # RAMA DERECHA (Surrealista):
        verso12 = FrasePayada("es que relinchó en la siesta.")
        verso13 = FrasePayada("¡pero el lucero me contesta...!")
        # Reutilización
        verso14 = verso12
        verso15 = verso13

        # Enlazar nodos manualmente (sig_izq / sig_der)
        
        verso1.sig_izq = verso2
        verso1.sig_der = verso3

        verso2.sig_izq = verso4
        verso2.sig_der = verso5

        verso3.sig_izq = verso6
        verso3.sig_der = verso7

        verso4.sig_izq = verso8
        verso4.sig_der = verso9

        verso5.sig_izq = verso8
        verso5.sig_der = verso9

        verso6.sig_izq = verso12
        verso6.sig_der = verso13

        verso7.sig_izq= verso14
        verso7.sig_der= verso15

        # Opciones iniciales
        opciones_nodos = [verso1]

        # Lista de frases elejidas
        payadaVega = []

    # Haremos exactamente 4 selecciones (4 niveles)
    $ rondas = 4
    $ nivel_actual = 1
    $ ambicion_resultante =0
    $ humildad_resultante =0
    
    play music paya_1_A volume 0.5 fadein 1

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
        $ ambicion_resultante += chosen.ambicion
        $ humildad_resultante += chosen.humildad

        python:
            # Ejemplo: almacenar en variables globales accesibles por Ren'Py
            store.ambicion = getattr(store, 'ambicion', 0) + chosen.ambicion
            store.humildad = getattr(store, 'humildad', 0) + chosen.humildad
            
        

        # Seleccionar musica segun nivel y encolar para transición suave
        if nivel_actual == 2:
            # stop music 
            play music paya_1_B volume 0.5 
        if nivel_actual == 3:
            # stop music 
            play music paya_1_A volume 0.5 
        if nivel_actual == 4:
            # stop music 
            play music paya_1_B volume 0.5  
            

        # Mostrar la payada actualizada
        $ payada_texto = "\n".join([f.MostrarFrase() for f in payadaVega])
        $ san("[payada_texto]", interact=False)

        # Reinicio la lista de texto para que se pueda leer
        if nivel_actual == 4:
            $ san("[payada_texto]")
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
    payador "¡Ahora si, Vega, es momento para una buena payada!"
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
    narrator "Esa noche, entre risas, música y amigos, la sombra de la Salamanca se disolvió en el aire. Santos no ganó la fama eterna... pero ganó el poder descansar tranquilo."
    return