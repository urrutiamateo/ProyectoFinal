label payada_final_bueno_manager(musicPlaying=False):
    # inicia musica

    # if not musicPlaying:
    #     # play music payada_intensa volume 0.5 fadein 1.0
    #     play music paya_1_A volume 0.5 fadein 0


    play music paya_1_A volume 0.5 fadein 0.1
    call payada_final_bueno_vega
    queue music paya_1_final volume 0.5 fadein 0 noloop 
    
    
    call payada_final_bueno_payador
    queue music fin_payada_intensa volume 0.5 fadein 1.0 noloop
    
    call payada_final_bueno_terminar
    return
 
label payada_final_bueno_vega:
    # --- Construcción del árbol de payadas usando objetos FrasePayada ---
    python:
        # Importar solo la clase FrasePayada y construir nodos manualmente (sin ArbolPayadas)
        from python.payadas.FrasePayada import FrasePayada

        # Crear nodos (niveles: 1..4). Los leaves están en nivel 4.
        verso1 = FrasePayada("No fue miedo ni ambición,")
        
        verso2 = FrasePayada("fue el consejo del que amparo:")
        verso3 = FrasePayada("fue el alma la que mando,")
        
        verso4 = FrasePayada("no hay canto más fuerte, hermano,")
        verso5 = FrasePayada("no hay rumbo mas puro y claro")
        
        verso6 = FrasePayada("el diablo quiso mi canto,")
        verso7 = FrasePayada("el diablo cruzo mi paso,")

        verso8 = FrasePayada("que el que nace del alma libre.")
        verso9 = FrasePayada("que el que canta sin reparo.")

        verso10 = FrasePayada("pero el diablo paga caro.")
        verso11 = FrasePayada("que aquel que sigue su corazón.")

        verso12 = FrasePayada("y mi canto lo espantó.")
        verso13 = FrasePayada("y el corazón me habló.")

        verso14 = FrasePayada("y mi alma lo negó.")
        verso15 = FrasePayada("y mi voz lo condenó.")

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
        verso7.sig_izq = verso15

        # Opciones iniciales
        opciones_nodos = [verso1]

        # Lista de frases elejidas
        payadaVega = []

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
        # reinicio la lista de texto para que se pueda leer
        
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
        # Limpiar en caso de que hayan pasado 4
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
    return

label payada_final_bueno_payador:
    show rival_payador at right:
        ypos 1.1
        
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
    payador  "{cps=17}Si el diablo no te llevó, {w=0.5}\nfue porque tuvo templanza, {w=0.5}\no acaso el miedo, compadre, {w=0.5}\nte frenó la confianza."

    
    
    # jump fin_payada
    return


label payada_final_bueno_terminar:
    #hide show rival_payador
    #stop music fadeout 2.0
    show fondo_negro
    with dissolve
    play sound aplausos volume 0.7 fadein 0.5
    narrator "Y esa noche, entre amigos, risas, el vino y la guitarra, Santos entendió su destino.{w}No necesitaba fama ni gloria."
    narrator "Su canto ya era eterno… porque nacía de su alma libre."
    return