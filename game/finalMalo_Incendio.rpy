# Acá hacer el final del incendio


label final_malo_incendio:
    # "este es el final del incendio"
    
            
    stop music fadeout 1
    stop sound fadeout 1
    scene interiorPulperia_2
    hide pantalla_roja
    with dissolve

    play music misterio fadeout 2.0 fadein 2.0
    play sound murmullo volume 0.2 loop
    queue sound puerta volume 0.8

    show Incendio_santos_arrogante at left
        # linear 5 xpos 120
    with dissolve

    sanV "¡Buenas noches a la burrada! ¿Otra vez 
    papando moscas en este sucucho?"

    "Santos Vega entró altanero a la pulpería, ofendiendo a algunos de los payadores que frecuentaban la pulpería."

    show Incendio_payador_bebiendo at right
    with dissolve
    

    payador "¡Eh! Tranquilo, gaucho..."

    sanV "Ma' si, no llore' borrego."

    hide Incendio_payador_bebiendo
    show Incendio_payador_enojado at right
    with dissolve

    payador "No es manera de hablar a la paisanada..."

    menu:
        "Tranquilizar al payador.":
            sanV "Bueno bueno, mi amigo, no se ponga 
                fiero, al final de cuentas, debería 
                estar contento de tenerme acá. ¡Hasta 
                un aplauso merezco!"

            play sound sfx_murmuro_enojado volume 0.5
            payador "Es verdad, es un milagro 
                tenerlo con nosotros. De agrandado que 
                viene casi se atranca en la puerta..."

            hide Incendio_payador_enojado with dissolve

            sanV "Vaya tranquilo, 'amigo'..."

        "Ignorar al payador y seguir de farra.":
            hide Incendio_santos_arrogante
            show Incendio_santos_arrogante2 at left
            # El payador deja de pelear y se va
            hide Incendio_payador_enojado with dissolve
            show rival_payador:
                zoom 0.95
                yoffset 100
            with dissolve
            payador "Pesado..."
            hide rival_payador
            with dissolve


            sanV "¡Pulpero! Sirva una caña, me hace el 
                favor, que vengo cortando el viento 
                arriba del flete hace rato... Voy a 
                necesitar un trago si me van a hacer 
                hablar pavadas."
            
            "El viejo de la pulpería atiende el llamado de Santos Vega."

            show viejo_hablando at right 
            # with moveinright 
            with dissolve
            
            viejo "Si, muchacho, ya se lo alcanzo."
            hide viejo_hablando
            show viejo_en_la_pulperia at right

            play sound sfx_murmuro_viejo volume 0.5
            viejo "(Murmurando) Un trago va a necesitar seguro..."

            hide viejo_en_la_pulperia #desplazar


    show viejo_en_la_pulperia at right #desplazar
    viejo "Tome muchacho..."

    hide Incendio_santos_arrogante
    hide Incendio_santos_arrogante2
    show santos_con_cania at left

    sanV "Gracias, viejo."

    play sound sfx_sorbo volume 0.7

    hide santos_con_cania
    
    show Incendio_santos_arrogante at left
    with dissolve

    viejo "¡Qué bueno tenerlo acá!"
    hide Incendio_santos_arrogante
    show Incendio_santos_arrogante2 at left
    with dissolve

    sanV "Al fin se dan cuenta. 
    Si no fuera por este gaucho, la pulpería se viene abajo..."

    sanV "Deberían aprender estos payadores..."

    viejo "Permítame una pregunta..."

    hide Incendio_santos_arrogante2
    show Incendio_santos_arrogante at left
    with dissolve

    viejo "Alguien de su talento, de su altura, ¿tiene rival en las payadas?"

    sanV "Pero claro que no, como se atreve. 
    De norte a sur de esta provincia se escucha silencio si yo no canto."

    sanV "Desde el ser más luminoso al más oscuro yo lo paseo con la guitarra."

    viejo "¿Ah, sí? Hasta al diablo mismo parece que dijera..."

    sanV "¡Hasta al malo mismo!"

    hide viejo_en_la_pulperia
    show Incendio_viejo_demonio at right

    play music musica_mandinga fadein 0.1 volume 0.8
    play sound sfx_risa_mandinga volume 0.8

    diablo "Usté es un bocón Santos Vega, 
    más le vale que demuestre lo que dice."

    hide Incendio_santos_arrogante
    hide Incendio_santos_arrogante2 
    show Incendio_santos_asustado at left
    with dissolve

    play sound sfx_asustado volume 0.5

    sanV "¡Cosa e'Mandinga!"

    diablo "No es lo mismo llamar al diablo, que verlo venir"

    menu:
        "Intentar huir":

            diablo "Que pasa, Santito, ¿Está asustado?"
            hide Incendio_santos_asustado 
            show Incendio_santos_arrogante at left
            with dissolve

            sanV "A mí nadie me corre con la vaina."

            play sound sfx_risa_mandinga volume 0.8

            play sound sfx_murmuro_diabolico
            diablo "Esta vez andás equivocado, 
            te topaste con el facón de frente."


            pass
        "Hacerle frente al viejo":
            hide Incendio_santos_asustado 
            show Incendio_santos_arrogante at left
            with dissolve

            sanV "A vos no te debo nada, viejo. 
            Y si te sobra guapura, plantate a una payada."

            play sound sfx_risa_mandinga volume 0.8

            diablo "Payá si querés, así me divierto un rato."

            hide Incendio_santos_arrogante 
            show santos_payando at left
            with dissolve
            
            play music paya_1_AyB fadein 0.1 volume 0.8

            menu:
                "Frase romántica":
                    sanV "Le dije a mi china que vuelva, 
                        pero no quiso saber nada.."
                "Frase épica":
                    sanV "Yo soy la nube cercana, 
                        que en la desierta llanura.."

            stop music
            play sound sfx_guitarra_rota
            pause 0.5
            hide santos_payando
            show Incendio_santos_rompeGuitarra at left
            pause 5
            play music musica_mandinga fadein 1 volume 0.8

            sanV "¡Mi guitarra!"
            
            sanV "¡Esto ha sido obra maligna!"
            play sound sfx_risa_mandinga volume 0.8

            # hide santos_guitarra_rota
            # show santos_arrogante_1 at left:
            #     zoom 0.75
    
            # pass
    
    

    # diablo "No hay fuego que arda suficiente, \n
    # para apaciguar a quien ya perdió a su alma."

    play sound sfx_puertas_cerrando volume 2

    diablo "Ahora sí que estás jugado."

    queue sound sfx_asustado volume 0.7

    # Si eligio opcion A viene de Santos Arrogante
    # Si eligio opcion b viene de santos guitarra rota
    hide Incendio_santos_rompeGuitarra
    hide Incendio_santos_arrogante
    show Incendio_santos_asustado at left
    pass

    sanV "¡Las puertas! ¡¿Qué clase de gualicho es éste?!"

    sanV "¡Mejor quédese tranquilo! ¡Estamos entre peones inocentes!"


    diablo "Usté sigue sin entender, Santos. 
    Esta gente son la yapa, que me gano por impaciente."

    play sound sfx_risa_mandinga volume 0.8
    diablo "Y tu fama ya la perdiste, por jugarla de insolente."

    jump exterior_pulperia_incendio

    # play sound sfx_murmuro_diabolico
    # diablo "*murmuro inentendible*"

    # play sound sfx_fuego_crepitar 

    # sanV "¡Fuego!"

    # show fuego at right:
    #     zoom 0.2
    # show fuego at left:
    #     zoom 0.2
    # pause 5

    # play sound sfx_grito_derrota
    # sanV "¡Me lleva mandinga!"

    # # "mostrar exterior"

    # jump exterior_pulperia_incendio

label exterior_pulperia_incendio:
    scene pulperia_incendio
    with fade
    play sound sfx_fuego_exterior loop

    "La pulpería ardió hasta los cimientos, 
    silenciando risas y guitarras por igual. 
    La ambición de Santos Vega, 
    se pagó con la sangre de todos. 
    Porque Mandinga nunca da vuelto... 
    siempre se cobra con yapa."

    scene black
    show text "{size=80}FIN: Final Incendio{/size}" at truecenter
    with slowfade
    pause 3
    stop sound fadeout 6
    jump creditos_narrativa
    return









    

