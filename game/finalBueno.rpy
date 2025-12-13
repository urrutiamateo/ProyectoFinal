label final_bueno:
    #ESCENA 1 VIAJE DE REGRESO ##############################################################################
    #pause 0.5
    #scene viaje with fade
    #play sound campo_noche volume 0.5 fadein 1.0 loop
    #play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0
    #show santos_en_viaje at center

    

    

    #ESCENA 2 EXTERIOR PULPERIA ##############################################################################

    pause 0.5
    scene exteriorPulperia
    with fade
    play sound caballo_galope volume 0.3 fadein 1.0 
    play music misterio volume 0.5 fadein 1.0
    pause 4
    show santos_ext_pulperia at right:
        xpos 2300        # FUERA de cámara a la derecha
        linear 4 xpos 1920  # posición final dentro a la derecha
        
    with dissolve
    stop sound fadeout 2.0

    #"Las noches de Santos podrían haber estado llenas de reconocimiento y fama. Pero en cambio se convirtieron en momentos de tranquilidad y diversión."
    play sound murmullo volume 0.3 loop 
    san "Tanto estuve buscando ser el mejor cantor, que casi me olvido por qué canto." 

    san "El canto no es pa' la fama, es pa' compartir la pena, el vino y la risa entre amigos. "
    
    play sound murmullo volume 0.2 loop 
    san "El cantor fiel a su alma, nunca pierde en esta gran payada que es la vida."

    hide santos_ext_pulperia
    with dissolve
    #pause 0.3
    #play sound puerta volume 0.3
    stop sound fadeout 2.0
    play music misterio volume 0.5 fadeout 2.0 fadein 1.0

    #ESCENA 3 INTERIOR PULPERIA ##############################################################################
    scene interiorPulperia_2
    with fade
    play sound puerta volume 0.3
    #pause 0.3
    #play sound murmullo volume 0.4  
    queue sound murmullo loop volume 0.1
    show santos_entra_izquierda at left:
        linear 5 xpos 120
    with dissolve

    "La pulpería es un nido de risas y humo... hasta que la figura de Santos cruza el umbral."
    # stop music fadeout 1.5
    stop sound fadeout 1.5
    #play sound ohhh_pulperia volume 0.5 fadein 0.5
    play sound sfx_asustado volume 0.7

    show rival_payador at right:
        ypos 1.1
    with dissolve
    payador "¡Mírenlo! Dicen que el Mandinga te ofreció “la gloria”, Santos. "
    payador "¿Es verdad o volviste con la cola entre las patas?"

    # play music misterio volume 0.5 fadein 1.0
    san "No hay criollo que no tenga como faro, los recuerdos de su padrino. Esos lo llevan a la gloria a uno."
    
   
    payador "¡Andá! ¡Mirá qué poeta el Santos! A ver si todavía podés acompañar esos versos con la guitarra."
    play sound murmullo loop volume 0.1
    menu:
        "Aceptar el duelo al payador.":
            python:
                subir_ambicion()
            san "¡Vamos, pasame la guitarra, amigo! ¿Qué esperás?"
            
            jump payada_final_bueno
        "Embriagarse primero y luego aceptar el duelo.":
            python:
                subir_humildad()
            san "La guitarra no se va a ir a ningún lado. Primero voy a curarme el garguero del calor que hacía allá..."
            
            jump escena_final_bueno_ebrio
   

    #ESCENA 3A PAYADA SERIA FINAL BUENO ##############################################################################
    label payada_final_bueno:
    stop sound fadeout 1.5
    # play music payada_intensa volume 0.5 fadeout 2.0 fadein 2.0
    #play music payada_intensa volume 0.5 fadein 0.5
    scene interiorPulperia_2
    #with fade
    # play music "pruebaSantosVega.mp3" volume 0.2
    hide santos_entra_izquierda
    with dissolve
    
    show santos_payando at left
    with dissolve
    #"Santos acepta con orgullo el duelo, sereno pero con voz firme, no vacila..."
    

    call payada_final_bueno_manager(musicPlaying=True) from _call_payada_final_bueno_manager
    
    
    #"Santos siente orgullo, rodeado de aplausos y risas. Su canto no busca vencer, sino unir. Ha encontrado su verdadera victoria."
    
    #hide santos_payando
    #hide payador_cantando
    #hide fondo_negro
    #with dissolve
    pause 1
    scene pantalla_negra
    with slowfade
    

    #stop music
    jump escena_final_rancho

    #ESCENA 3B PAYADA GRACIOSA FINAL BUENO ##############################################################################
    label escena_final_bueno_ebrio:
        stop sound fadeout 1.5
        scene interiorPulperia_1
        with fade
        hide santos_entra_izquierda
        with dissolve
        show santos_con_cania at left
        with dissolve
        "Esa noche Santos dejó de lado la gloria y volvió a lo que siempre fue suyo: la risa entre amigos, el vino y la guitarra. "
        #"En ese bullicio que tanto extrañaba, entendió que ningún diablo vale más que un buen rato en la pulpería."
        #play sound aplausos volume 0.5 fadein 0.5
        
        
        call payada_final_bueno_ebrio_manager(musicPlaying=False) from _call_payada_final_bueno_ebrio_manager
       
        #"Santos siente orgullo, rodeado de aplausos y risas. Su canto no busca vencer, sino unir. Ha encontrado su verdadera victoria."
        #hide santos_payando
        #hide payador_cantando
        #scene pantalla_negra 
        #with slowfade
        pause 1
        scene pantalla_negra
        with slowfade
        
    
    #ESCENA FINAL RANCHO ##############################################################################
    label escena_final_rancho:
        scene rancho_amanecer with fade
        play sound campo_dia volume 0.3 fadein 1.0 loop
        play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0
        "Santos ahora canta con el alma en la voz, renacida en aquellas tinieblas, ahora más fuerte, más libre y fiel a sus raíces."
        "El pago lo vio renacer: sereno y humilde."
        "Porque el diablo podrá ofrecerlo todo… pero el canto libre no se negocia."
        stop music
        stop sound
        scene black
        show text "{size=80}FIN: Final Bueno.{/size}" at truecenter
        with slowfade
        pause 3
        jump creditos_narrativa
    #return
        #jump creditos_produccion

    #ESCENA FINAL CREDITOS ##############################################################################
    #label creditos_finales:
        #stop music
        #stop sound
        #scene pantalla_negra
        #with fade
        #"FIN"
        #jump creditos_produccion