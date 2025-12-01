label final_malo_ombu_2:
    
    stop sound fadeout 1
    stop music fadeout 1
    # Parte 1
    scene ombu
    show santos_durmiendo_ombu

    hide pantalla_roja 
    with dissolve

    play audio campo_dia volume 0.2 fadein 1.0 loop
    play audio sfx_afligido volume 0.9

    sanV "No... No... Padrino... Sangre... Ayúdeme..."

    play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0

    play audio sfx_pasos_pasto volume 0.9

    pause 3

    show juan_hablando at right:
            zoom 1.25
    juan_oculto "Disculpe, muchacho..."
  
    hide santos_durmiendo_ombu
    show santos_recostado at left

    sanV "¿Qué quiere hombre?"

    juan_oculto "¡Abrió sus ojos risueños! Estoy 
                buscando a Santos Vega. Desde lejos 
                vengo preguntando..."

    juan_oculto "Pasé recién por un poblado vecino y me 
                han dicho que hace tiempo a su mejor 
                cantor, Santos lo ha humillado. ¡Qué 
                pena por el pobre gaucho!"
    
    # Parte 2
    menu: 
        "Averiguar que busca el paisano.":
            sanV "No se deje engañar, no todos son tan 
                fieros como parece. Cualquiera puede 
                perder si anda poco avispado."
            juan_oculto "En eso tiene razón, amigo. Yo estoy
                        buscando con quien payar y mejorar mi 
                        canto."
            sanV "Tóquese algo paisano, y cuente lo que 
                tiene para decir."
            pass 
        "Aceptar el reconocimiento.":
            sanV "¡A ese ya lo humillé hace rato! Y a 
                pesar de que, en ese entonces, todavía 
                no era tan bueno en el canto."
            juan_oculto "Parece que no se dedica a otra cosa 
                        que no sea la guitarra..."
            sanV " Puedo pecar de talentoso, pero no de 
                abandonado..."
            juan_oculto "Le propongo payar, a ver quien sale 
                ganado."
            sanV "Empiece cuando quiera, de acá acostado 
                lo escucho..."

    hide juan_hablando
    show juan_guitarra at right:
        zoom 1.25
    play music payada_intensa volume 0.5 fadeout 0.5 fadein 0.5


    juan_oculto "{cps=17}{w=1 }Deje que agarre paisano,{w=2} a la 
                corrida... mi guitarra. {w=1}Que tengo un 
                chichón en la frente...{w=2} y una canción 
                en la maaaaanooooo..."

    stop music fadeout 2

    play sound sfx_risa_hombre

    sanV "Ja ja ja..."

    sanV "Yo le voy a enseñar cuantos pares son tres botas."
    
    hide juan_guitarra
    show juan_hablando at right:
        zoom 1.25


    hide santos_recostado
    show santos_payando at left
    with dissolve

    call payada_ombu(musicPlaying=True) from _call_payada_ombu_2

    play music musica_mandinga fadein 0.1 volume 0.9


    play sound sfx_indignado
    san"¡Lo suyo fue un engaño!, 
    esos versos no son de borrego en el canto. 
    Diga entero su nombre, 
    si no quiere terminar apuntalado."
    
    play sound sfx_risa_diabolica

    juan "No hay facón que me alcance, 
    no soy hombre ni sombra, {w=0.5}{cps=17}{b}soy Juan Sin Ropa. 
    Y vengo a cobrarme su alma empeñada.{/b}"

    play sound sfx_grunido

    sanV "¡No me voy a ir sin pelearla!"
    # hide santos_hablando_guitarra
    # show santos_payando at left
    
    # define config.menu_clear_window = False
    play music paya_1_A volume 0.8
    menu: 
        "Bajo el Ombú solitario":
            # renpy.say(sanV,"Bajo el Ombú solitario",False)
            sanV "Bajo el Ombú solitario" 
        "Como un eco del quebranto":
            # renpy.say(sanV,"Como un eco del quebranto",False)
            sanV "Como un eco del quebranto"
    queue music paya_1_B volume 0.8
    menu: 
        "Cruza el viento temerario.":
            sanV "Cruza el viento temerario."
        "Mi canto al cielo levanto.":
            sanV "Mi canto al cielo levanto."
    
    stop music
    play sound sfx_guitarra_rota

    hide santos_payando
    show Incendio_santos_rompeGuitarra at left
    
    
    
    sanV "¡Cosa e 'Mandinga!"
    play music musica_mandinga fadein 0.2 volume 0.8

    sanV "¡Mi guitarra! ¿Qué le hiciste?"

    play sound sfx_risa_jactante
    hide juan_guitarra
    show juan_hablando at right:
        zoom 1.25
    with dissolve

    juan "Se acabó tu gloria, Santos. {w=0.5}De esta no safaste ni cantando."

    hide juan_hablando with dissolve
    show serpiente_ombu at right
    with dissolve
    play sound serpiente volume 0.3
    pause 3
    hide Incendio_santos_rompeGuitarra with dissolve
    queue sound sfx_grito_derrota volume 0.8 fadein 2

    pause 2

    # hide serpiente_ombu with dissolve
    hide serpiente_ombu with dissolve
    show serpiente at right:
        zoom 1.6
        linear 8 yoffset 600 xoffset -2500 zoom 2 
    with dissolve

    pause 10

    # show serpiente at left
    # with dissolve
    # pause 1
    # hide serpiente
    # with dissolve
    # pause 0.5

    # show serpiente_ombu at right:
    #     linear 10 yoffset -100 xoffset 0 zoom 1.0  
        
    
    narrator "El canto del que firma el pacto, 
            queda sellado como su destino."
    #narrator "El canto vanidoso nunca encontrará la paz."



    scene black
    show text "{size=80}FIN: Final Ombú{/size}" at truecenter
    with slowfade
    pause 3
    jump creditos_narrativa
    return