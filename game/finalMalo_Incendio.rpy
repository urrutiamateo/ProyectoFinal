# Acá hacer el final del incendio
label final_malo_incendio:
    # "este es el final del incendio"


            

    scene interiorPulperia_2
    play music misterio fadeout 2.0 fadein 2.0
    play sound murmullo volume 0.2 loop
    queue sound puerta volume 0.8

    show santos_arrogante_1 at left:
        # linear 5 xpos 120
        zoom 0.6
    with dissolve

    san "¡Buenas noches a la burrada! ¿Otra vez 
    papando moscas en este sucucho?"

    show payador_sentado at right:
        # linear 5 xpos 120
        zoom 0.8
    with dissolve

    payador "¡Eh! Tranquilo, gaucho..."

    san "Ma' si, no llore' borrego."

    hide payador_sentado
    show payador_enojado at right:
        # linear 5 xpos 120
        zoom 0.8
    with dissolve

    payador "No es manera de hablar a la paisanada..."

    menu:
        "Tranquilizar al payador.":
            san "Bueno bueno, mi amigo, no se ponga 
                fiero, al final de cuentas, debería 
                estar contento de tenerme acá. ¡Hasta 
                un aplauso merezco!"

            play sound sfx_murmuro_enojado volume 0.5
            payador "(Murmurando) Es verdad, es un milagro 
                tenerlo con nosotros. De agrandado que 
                viene casi se atranca en la puerta..."

            hide payador_enojado

            san "Vaya tranquilo, 'amigo'..."

        "Ignorar al payador y seguir de farra.":
            hide santos_arrogante_1
            show santos_arrogante_2 at left:
                # linear 5 xpos 120
                zoom 0.6
            # El payador deja de pelear y se va
            hide payador_enojado
            show rival_payador:
                zoom 0.8
            with dissolve
            payador "Pesado..."
            hide rival_payador

            san "¡Pulpero! Sirva una caña, me hace el 
                favor, que vengo cortando el viento 
                arriba del flete hace rato... Voy a 
                necesitar un trago si me van a hacer 
                hablar pavadas."

            show viejo_hablando at right
            with dissolve
            
            viejo "Si, muchacho, ya se lo alcanzo."
            hide viejo_hablando
            show viejo_en_la_pulperia at right

            play sound sfx_murmuro_viejo volume 0.5
            viejo "(Murmurando) Un trago va a necesitar seguro..."

            hide viejo_en_la_pulperia #desplazar


    show viejo_en_la_pulperia at right #desplazar
    viejo "Tome muchacho..."

    hide santos_arrogante_1
    hide santos_arrogante_2
    show santos_con_cania at left

    san "Gracias, viejo."

    play sound sfx_sorbo volume 0.7

    hide santos_con_cania
    
    show santos_arrogante_1 at left:
    # linear 5 xpos 120
        zoom 0.6
    with dissolve

    viejo "¡Qué bueno tenerlo acá!"
    hide santos_arrogante_1
    show santos_arrogante_2 at left:
    # linear 5 xpos 120
        zoom 0.6
    with dissolve

    san "Al fin se dan cuenta. 
    Si no fuera por este gaucho, la pulpería se viene abajo..."

    san "*Dirigiéndose a los Payadores* Aprendan un poco ustedes..."

    viejo "Permítame una pregunta..."

    hide santos_arrogante_2
    show santos_arrogante_1 at left:
    # linear 5 xpos 120
        zoom 0.6
    with dissolve

    viejo "Alguien de su talento, de su altura, ¿tiene rival en las payadas?"

    san "Pero claro que no, como se atreve. 
    De norte a sur de esta provincia se escucha silencio si yo no canto."

    san "Desde el ser más luminoso al más oscuro yo lo paseo con la guitarra."

    san "¿Ah, sí? Hasta al diablo mismo parece que dijera..."

    san "¡Hasta al malo mismo!"

    hide viejo_en_la_pulperia
    show viejo_diabolico at right:
        ypos 1500

    play music musica_mandinga fadein 0.1 volume 0.8
    play sound sfx_risa_mandinga volume 0.8

    diablo "Usté es un bocón Santos Vega, 
    más le vale que demuestre lo que dice."

    hide santos_arrogante_1
    hide santos_arrogante_2 
    show santos_asustado at left:
        zoom 0.6
    with dissolve

    play sound sfx_asustado volume 0.5

    san "¡Cosa e'Mandinga!"

    diablo "No es lo mismo llamar al diablo, que verlo venir"

    menu:
        "Intentar huir":

            diablo "Que pasa, Santito, ¿Está asustado?"
            hide santos_asustado 
            show santos_arrogante_1 at left:
                zoom 0.6
            with dissolve

            san "A mí nadie me corre con la vaina."

            play sound sfx_risa_mandinga volume 0.8

            diablo "Esta vez andás equivocado, 
            te topaste con el facón de frente."


            pass
        "Hacerle frente al viejo":
            hide santos_asustado 
            show santos_arrogante_1 at left:
                zoom 0.6
            with dissolve

            san "A vos no te debo nada, viejo. 
            Y si te sobra guapura, plantate a una payada."

            play sound sfx_risa_mandinga volume 0.8

            diablo "Payá si querés, así me divierto un rato."

            hide santos_arrogante_1 
            show santos_payando at left:
                zoom 0.6
            with dissolve
            
            play music paya_1_AyB fadein 0.1 volume 0.8

            menu:
                "Frase romántica":
                    san "Le dije a mi china que vuelva, 
                        pero no quiso saber nada.."
                "Frase épica":
                    san "Yo soy la nube cercana, 
                        que en la desierta llanura.."

            stop music
            play sound sfx_guitarra_rota
            pause 0.5
            hide santos_payando
            show santos_guitarra_rota at left:
                zoom 0.75
            pause 5
            play music musica_mandinga fadein 1 volume 0.8

            san "¡Mi guitarra!"
            
            san "¡Esto ha sido obra maligna!"
            play sound sfx_risa_mandinga volume 0.8

            # hide santos_guitarra_rota
            # show santos_arrogante_1 at left:
            #     zoom 0.75
    
            # pass
    
    play sound sfx_murmuro_diabolico

    diablo "*murmuro inentendible*"

    play sound sfx_puertas_cerrando volume 2

    diablo "Ahora sí que estás jugado."

    queue sound sfx_asustado volume 0.7

    # Si eligio opcion A viene de Santos Arrogante
    # Si eligio opcion b viene de santos guitarra rota
    hide santos_guitarra_rota
    hide santos_arrogante_1
    show santos_asustado at left:
        zoom 0.75
    pass

    san "¡Las puertas! ¡¿Qué clase de gualicho es este?!"

    san "¡Mejor quédese tranquilo! ¡Estamos entre peones inocentes!"


    diablo "Usté sigue sin entender Santos. 
    Estas gentes son la yapa, que me gano por impaciente."

    play sound sfx_risa_mandinga volume 0.8
    diablo "Y tu fama ya la perdiste, por jugarla de insolente."

    play sound sfx_murmuro_diabolico
    diablo "*murmuro inentendible*"

    play sound sfx_fuego_crepitar 

    san "¡Fuego!"

    show fuego at right:
        zoom 0.2
    show fuego at left:
        zoom 0.2
    pause 5

    play sound sfx_grito_derrota
    san "¡Me lleva mandinga!"

    "mostrar exterior"

    jump exterior_pulperia_incendio

label exterior_pulperia_incendio:
    scene pulperia_incendio
    play sound sfx_fuego_exterior loop

    "La pulpería ardió hasta los cimientos, 
    silenciando risas y guitarras por igual. 
    La ambición de Santos Vega, 
    se pagó con la sangre de todos. 
    Porque Mandinga nunca da vuelto... 
    siempre se cobra con yapa."

    scene black
    show text "{size=80}FIN: Final Ombú{/size}" at truecenter
    with slowfade
    pause 3
    jump creditos_produccion
    return









    

