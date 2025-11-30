# Acá hacer el final del incendio
label final_malo_incendio:
    # "este es el final del incendio"


    scene interiorPulperia_2
    play music misterio fadeout 2.0 fadein 2.0
    play sound murmullo volume 0.2 loop

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

    san "(Dirigiéndose a los Payadores) Aprendan un poco ustedes..."

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
            pass
        "Hacerle frente al viejo":
            pass







    

