label payada_ombu(musicPlaying=False):
    # inicia musica

    # if not musicPlaying:
    #     # play music payada_intensa volume 0.5 fadein 1.0
    #     play music paya_1_A volume 0.5 fadein 0

    play music paya_1_A volume 0.5 fadein 0.1
    call payada_vega_ombu
    queue music paya_1_final volume 0.5 fadein 0 noloop
    hide santos_payando

    call payada_JuanSinRopa
    play music fin_payada_intensa volume 0.5 fadein 1.0 noloop

    return


label payada_vega_ombu:
    # --- Construcción del árbol de payadas usando objetos FrasePayada ---
    python:
        # Importar solo la clase FrasePayada y construir nodos manualmente (sin ArbolPayadas)
        from python.payadas.FrasePayada import FrasePayada

        verso1 = FrasePayada("Bajo el ombú solitario,")
        verso2 = FrasePayada("mi canto al cielo levanto,")
        verso3 = FrasePayada("como un eco de mi quebranto,")
        verso4 = FrasePayada("cruza el viento temerario.")
        verso5 = FrasePayada("Soy cantor, y es mi calvario")
        verso6 = FrasePayada("la pasión que me ilumina;")
        verso7 = FrasePayada("mi voz por la pampa trina,")
        verso8 = FrasePayada("se confunde con el viento,")

        verso9 = FrasePayada("y hasta el silencio violento")
        verso10 = FrasePayada("me respeta en su doctrina.")

        verso11 = FrasePayada("tiembla el canto en mi garganta,")
        verso12 = FrasePayada("la noche calla y espanta,")
        verso13 = FrasePayada("presagiando mi calvario.")
        verso14 = FrasePayada("Soy cantor, y mi adversario")
        verso15 = FrasePayada("desafía mi desvelo,")
        verso16 = FrasePayada("su voz sube hasta el anhelo")
        verso17 = FrasePayada("donde el alma se desgrana,")

        verso18 = FrasePayada("y en la pampa sobrehumana")
        verso19 = FrasePayada("se confunden cielo y duelo.")

        # Enlazar nodos manualmente (sig_izq / sig_der)

        verso1.sig_izq = verso2
        verso2.sig_izq = verso3
        verso3.sig_izq = verso4
        verso4.sig_izq = verso5
        verso5.sig_izq = verso6
        verso6.sig_izq = verso7
        verso7.sig_izq = verso8
        verso8.sig_izq = verso9
        verso9.sig_izq = verso10

        verso1.sig_der = verso11
        verso11.sig_der = verso12
        verso12.sig_der = verso13
        verso13.sig_der = verso14
        verso14.sig_der = verso15
        verso15.sig_der = verso16
        verso16.sig_der = verso17
        verso17.sig_der = verso18
        verso18.sig_der = verso19

        #opciones iniciales
        opciones_nodos = [verso1]

        # Lista de frases elejidas
        payadaVega = []    
        ambicion_total = 0
        humildad_total = 0


    # Haremos exactamente 10 selecciones (10 niveles)
    # --- Configuración de rondas ---
    # --- Configuración de rondas ---
    $ rondas = 10
    $ nivel_actual = 1

    while nivel_actual <= rondas:

        # --- Construir menú con las opciones actuales (pueden ser 1 o 2) ---
        python:
            menu_items = []
            for n in opciones_nodos:
                if n is None:
                    continue
                menu_items.append((n.MostrarFrase(), n))

            if not menu_items:
                chosen = None
            else:
                chosen = renpy.display_menu(menu_items)

        if chosen is None:
            $ nivel_actual = rondas + 1
        else:
            # --- Registrar la elección ---
            $ payadaVega.append(chosen)

            # --- Determinar el bloque actual de 4 versos ---
            python:
                # Bloque de 4 (1–4, 5–8, 9–12, etc.)
                bloque_inicio = ((nivel_actual - 1) // 4) * 4
                bloque_fin = bloque_inicio + 4
                versos_a_mostrar = payadaVega[bloque_inicio:bloque_fin]
                payada_texto = "\n".join([f.MostrarFrase() for f in versos_a_mostrar])

            san "[payada_texto]"

            # --- Actualizar los valores de ambición y humildad ---
            python:
                store.ambicion = getattr(store, 'ambicion', 0) + chosen.ambicion
                store.humildad = getattr(store, 'humildad', 0) + chosen.humildad

            # --- Seleccionar música según el nivel ---
            if nivel_actual == 2:
                queue music paya_1_B volume 0.5
            elif nivel_actual == 3:
                queue music paya_1_A volume 0.5
            elif nivel_actual == 4:
                queue music paya_1_B volume 0.5
            elif nivel_actual == 5:
                queue music paya_1_A volume 0.5
            elif nivel_actual == 6:
                queue music paya_1_B volume 0.5
            elif nivel_actual == 7:
                queue music paya_1_A volume 0.5
            elif nivel_actual == 8:
                queue music paya_1_B volume 0.5
            elif nivel_actual == 9:
                queue music paya_1_A volume 0.5
            elif nivel_actual == 10:
                queue music paya_1_B volume 0.5

            # --- Preparar las opciones del siguiente nivel ---
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
    show juan_guitarra at right
    juan "Yo vengo del polvo oscuro \nque el hombre teme y no nombra,\ndonde el alma pierde sombra, \ny el tiempo no tiene muro."
    juan "Traigo un eco frío y puro \nque ni Dios osa escuchar, \nmi copla no sabe amar, \nni tiene piedad ni pena:" 
    juan "\nsoy quien en la noche suena \ncuando cesa el respirar."
    juan "Tu voz, Santos, fue un lucero, \nmas toda luz tiene ocaso; \ntu canto, noble y escaso, \nya muere en su propio acero."
    juan "Yo soy viento y soy sendero, \nsoy silencio que no calla, \nmi copla en tu pecho estalla, \ny en la pampa queda escrito:" 
    juan "que quien canta al infinito \npierde el alma si la halla."
    return