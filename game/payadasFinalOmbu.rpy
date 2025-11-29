label payada_ombu(musicPlaying=False):
    # inicia musica

    # if not musicPlaying:
    #     # play music payada_intensa volume 0.5 fadein 1.0
    #     play music paya_1_A volume 0.5 fadein 0
    play music paya_2_intro  volume 0.5 fadein 0.1 noloop
    queue music paya_2_A volume 0.5 fadein 0.1
    call payada_vega_ombu from _call_payada_vega_ombu
    queue music paya_2_Final volume 0.5 fadein 0 noloop
    hide santos_payando

    call payada_JuanSinRopa from _call_payada_JuanSinRopa
    play music fin_payada_intensa volume 0.5 fadein 1.0 noloop

    return


label payada_vega_ombu:
    # --- Construcción del árbol de payadas usando objetos FrasePayada ---
    python:
        # Importar solo la clase FrasePayada y construir nodos manualmente (sin ArbolPayadas)
        from python.payadas.FrasePayada import FrasePayada

        verso1 = FrasePayada("La pampa sabe quien es dueño,")

        verso2 = FrasePayada("mi canto vuela y resplandece,")
        verso3 = FrasePayada("mi canto nunca se apaga,")
        
        verso4 = FrasePayada("el viento mismo me obedece,")
        verso5 = FrasePayada("en cada rincón se fortalece,")
        
        verso6 = FrasePayada("el viento lo lleva y embriaga,")
        verso7 = FrasePayada("lleva mi alma en su diseño,")

        verso8 = FrasePayada("y mi voz nunca pierde empeño.")
        verso9 = FrasePayada("y mi voz se alza como un sueño.")
        
        verso10 = FrasePayada("y la voz del viento lo enaltece.")
        verso11 = FrasePayada("y la libertad en mí florece.")

        verso12 = FrasePayada("y en cada rincón se propaga.")
        verso13 = FrasePayada("y mis versos a todos halagan.")

        verso14 = FrasePayada("y por el viento se propaga.")
        verso15 = FrasePayada("y la libertad en él se alza.")

        # Enlazar nodos manualmente (sig_izq / sig_der)

        verso1.sig_izq = verso2
        verso1.sig_der = verso3

        verso2.sig_izq = verso4
        verso2.sig_der = verso5

        verso3.sig_izq = verso6
        verso3.sig_der = verso7

        verso4.sig_izq = verso8
        verso4.sig_der = verso9

        verso5.sig_izq = verso10
        verso5.sig_der = verso11

        verso6.sig_izq = verso12
        verso6.sig_der = verso13

        verso7.sig_izq = verso14
        verso7.sig_der = verso15

        #opciones iniciales
        opciones_nodos = [verso1]

        # Lista de frases elejidas
        payadaVega = []

    # Haremos exactamente 4 selecciones (4 niveles)
    $ rondas = 4
    $ nivel_actual = 1
    $ ambicion_resultante =0
    $ humildad_resultante =0
    
    # play music paya_1_A volume 0.5 fadein 1

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
            play music paya_2_B volume 0.5 
        if nivel_actual == 3:
            play music paya_2_A volume 0.5 
        if nivel_actual == 4:
            play music paya_2_B volume 0.5 
            

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

label payada_JuanSinRopa:
    
    juan "Fue una gran payada, pero ahora es mi turno."
    hide juan_hablando with fade
    
    play music payada_intensa volume 0.5 fadeout 0.5 fadein 0.5
    show juan_guitarra at right:
        zoom 1.2
    juan "{cps=17} Yo vengo del polvo oscuro,{w=0.5}\ndonde el alma pierde el paso,{w=0.5}\nmi canto no tiene lazo,{w=0.5}\nni cielo, ni nombre puro."
    juan "{cps=17}Tu voz fue un fuego maduro,{w=0.5}\nmas todo fuego es escaso;{w=0.5}\ncantás, Santos, tu fracaso:{w=0.5}\nque el alma ya dio su paso."
    return