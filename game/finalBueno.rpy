label final_bueno:
    #ESCENA 1 VIAJE DE REGRESO ##############################################################################
    pause 0.5
    scene viaje with fade
    play sound brisa volume 0.3 fadein 1.0 loop
    play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0
    show santos_en_viaje at center

    "Dicen que esa noche el canto de Santos se perdió en la llanura, como si el viento pampeano al soplar se lo hubiera robado."

    "El Mandinga quedó atrás, entre las sombras, bajo la tierra. Santos cabalga con el corazón cansado, pero limpio." 
    
    "Observando el infinito cielo estrellado recuerda la frase de su viejo padrino:" 
    
    "“No hay canto más fuerte que el que nace del alma libre”."

    "Fue así que comprendió que no hay oro, fama o diablo que pueda comprar su libertad."

    "Y es entonces que su canto volvió a nacer más fuerte y más libre."

    #ESCENA 2 EXTERIOR PULPERIA ##############################################################################

    pause 0.5
    scene exteriorPulperia
    with fade
    play sound murmullo volume 0.3 loop 

    show santos_ext_pulperia at right
    with dissolve

    "Santos se detiene pensativo, su vida ya no sería la misma. Ahora cantará con el alma libre, honrando la memoria de su padrino."

    san "Tanto estuve buscando ser el mejor cantor, que casi me olvido por qué canto." 
    san "El canto no es pa´ la fama, es pa´compartir la pena, el vino y la risa entre amigos. El cantor fiel a su alma nunca pierde en esta gran payada que es la vida."

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
    queue sound murmullo loop volume 0.2
    show santos_entra_izquierda at left:
        linear 5 xpos 120
    with dissolve

    "Los gauchos beben, ríen, otros juegan a los naipes. Una guitarra pasa de mano en mano. De pronto se produce un silencio cuando lo ven entrar a Santos"
    "Los más curiosos le preguntan cómo fue su sombría travesía hacia la Salamanca. Otros lo acusan, sin saber, de ser socio del diablo."
    show rival_payador at right:
        ypos 1.1
    with dissolve
    payador "¡Miren quién volvió de la Salamanca! Santos, dicen que el Mandinga te ofreció fama y gloria, ¡contanos!"

    san "Así fue, pero aprendí una gran lección, la libertad no tiene precio y preferí venir a cantar entre amigos!"

    payador "¡Dale, entonces mostranos lo que aprendiste, Santos! A ver si tu voz ahora suena diferente, ¡veamos quién es mejor payador!"

    menu:
        "Aceptar el duelo al payador.":
            "Santos acepta el duelo, ahora demostrará que se puede ser fiel a su propio talento y lograr reconocimiento también..."
            stop sound fadeout 1.5
            jump payada_final_bueno
        "Embriagarse primero y luego aceptar el duelo.":
            "Santos después de un estresante viaje a la mismísima cueva del diablo, decide embriagarse primero..."
            stop sound fadeout 1.5
            jump escena_final_bueno_ebrio
   

    #ESCENA 3A PAYADA SERIA FINAL BUENO ##############################################################################
    label payada_final_bueno:
    # play music payada_intensa volume 0.5 fadeout 2.0 fadein 2.0
    #play music payada_intensa volume 0.5 fadein 0.5
    scene interiorPulperia_2
    #with fade
    # play music "pruebaSantosVega.mp3" volume 0.2
    hide santos_entra_izquierda
    with dissolve
    
    show santos_payando at left
    with dissolve
    "Santos acepta con orgullo el duelo, sereno pero con voz firme, no vacila..."
    "y canta con su alma en la voz renacida en aquellas tinieblas, ahora más fuerte, más libre y fiel a sus raíces."

    call payada_final_bueno_manager(musicPlaying=True) from _call_payada_final_bueno_manager
    
    "Santos siente orgullo, rodeado de aplausos y risas. Su canto no busca vencer, sino unir. Ha encontrado su verdadera victoria."
    #hide santos_payando
    #hide payador_cantando
    #hide fondo_negro
    with dissolve
    scene pantalla_negra
    with fade

    stop music
    jump escena_final_rancho

    #ESCENA 3B PAYADA GRACIOSA FINAL BUENO ##############################################################################
    label escena_final_bueno_ebrio:
        scene interiorPulperia_1
        with fade
        hide santos_entra_izquierda
        with dissolve
        show santos_con_cania at left
        with dissolve
        "Santos esa noche decidió olvidarse de ser el mejor payador, se dedica a beber un buen rato y a charlar con amigos."
        "Santos extrañaba ese bullicio de la pulpería, las risas, acompañados de música y canto."
        "Finalmente es momento de una divertida payada."
        
        
        call payada_final_bueno_ebrio_manager(musicPlaying=False) from _call_payada_final_bueno_ebrio_manager
       
        "Santos siente orgullo, rodeado de aplausos y risas. Su canto no busca vencer, sino unir. Ha encontrado su verdadera victoria."
        #hide santos_payando
        #hide payador_cantando
        scene pantalla_negra 
        with slowfade
        
    
    #ESCENA FINAL RANCHO ##############################################################################
    label escena_final_rancho:
        scene exteriorRanchoNoche with fade
        play sound brisa volume 0.3 fadein 1.0 loop
        play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0
        "Y dicen que aquella noche,entre vino y carcajadas,Santos Vega volvió a ser cantor libre en alma y en payadas."
        "El pago lo vio distinto, más sereno, más humano. Ya no buscaba laureles, solo la calidez del paisano."
        "Porque el diablo puede ofrecer oro, fama o poder, pero el alma que no se vende, vale más que cualquier talento."
        stop music
        stop sound
        jump creditos_produccion

    #ESCENA FINAL CREDITOS ##############################################################################
    #label creditos_finales:
        stop music
        stop sound
        scene pantalla_negra
        with fade
        "FIN"
        jump creditos_produccion