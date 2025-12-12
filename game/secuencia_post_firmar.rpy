label viaje_post_firmar:
    stop sound fadeout 1.0
    stop music fadeout 2.0
    play music paya_2_Completa volume 1 fadeout 0.1 fadein 0.1
    scene viaje with fade

    play sound brisa volume 0.8 fadein 1.0 loop
    

    narrator "Santos Vega se convirtió en el mejor payador, 
    hechizaba a todos con su canto. 
    Iba de pueblo en pueblo 
    y nadie quedaba sin escucharlo."

    "Una madrugada, mientras Santos Vega duerme 
    entre viaje y viaje, en sus oscuros sueños 
    oye voces."

    #show pantalla_gris:
    #    alpha 0.0
    #    linear 1.0 alpha 0.7  # sube opacidad a 0.5 en 1 segundo
    
    pause 2
    jump recuerdo_mandinga
    
label recuerdo_mandinga:
    scene trono_mandinga 
    show overlay_pesadilla onlayer dreamlayer
    with irisout
    pause 0.1
    
    #hide pantalla_gris

    play music musica_mandinga volume 0.5 fadeout 2.0 fadein 1.0
    play sound latidos_completo volume 0.5

    voz_sueño1 "{color=#f5272e}{i}¿Qué desea el que me busca?{/i}{/color}"

    voz_sueño2 "{color=#F5D627}{i}Hechizar la pampa con mi canto.{/i}{/color}"

    voz_sueño1 "{color=#f5272e}{i}Pero eso cuesta... el alma. ¿Estás dispuesto…?{/i}{/color}"

    voz_sueño2 "{color=#F5D627}{i}¿Adónde hay que firmar?{/i}{/color}"

    scene contratoFirmado 
    with fade

    narrator "Toda promesa tiene un precio. 
    Y en sus sueños, Santos Vega comenzó a pagarlo. 
    Sus pesadillas lo perseguían hasta abajo de la cama. 
    La pampa escuchó su canto, pero también su condena..."
    hide overlay_pesadilla onlayer dreamlayer
    with dissolve
    
    ##CHORREA SANGRE EN LA PANTALLA
    show sangre at truecenter
    play sound suspiro_scare volume 0.5
    #with dissolve
    pause 0.25
    #hide sangre
    #with dissolve

    show pantalla_roja # onlayer dreamlayer
    with fade 
        #alpha 0.0
        #linear 1 alpha 1  # sube opacidad a 0.7 en 1.5 segundos

    

    # LÓGICA DE DECISIÓN DE FINALES
    # si la Humildad es mayor o igual a la Ambición, va al final del ombú.
    if humildad >= ambicion:
        
        "Esas pesadillas lo castigaban a Santos Vega."
        pause 1
        stop sound fadeout 1
        jump final_malo_ombu_2

    # si la Ambición es mayor que la humildad, va al final del incendio.
    else:
        "Ese castigo no es nada comparado con su deuda."
        pause 1
        stop sound fadeout 1
        jump final_malo_incendio
    #jump final_malo_ombu
