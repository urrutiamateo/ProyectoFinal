label viaje_post_firmar:
    stop sound fadeout 1.0
    stop music fadeout 2.0
    play music paya_2_Completa volume 1 fadeout 0.1 fadein 0.1
    scene viaje with fade

    play sound brisa volume 0.8 fadein 1.0 loop
    

    narrator "La pampa entera se rindió ante su guitarra. De fogón en fogón, Santos Vega 
    tejía un hechizo del que nadie quería escapar. Y no hubo rincón del pago que no conociera su nombre."
    narrator "Pero la noche siempre cobra su parte. Una madrugada, cuando el cansancio lo venció en el camino, 
    {color=#f5272e}{b}en sus oscuros sueños, oyó voces.{/b}"

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

    voz_sueño2 "{color=#F5D627}{i}Hechizar la Pampa con mi canto.{/i}{/color}"

    voz_sueño1 "{color=#f5272e}{i}Pero eso cuesta el alma. ¿Estás dispuesto?{/i}{/color}"

    voz_sueño2 "{color=#F5D627}{i}¿A dónde hay que firmar?{/i}{/color}"

    scene contratoFirmado 
    with fade

    narrator "Toda promesa tiene un precio. 
    Y en sus sueños, Santos Vega comenzó a pagarlo. 
    Aquellas voces eran el eco de las sombras que ahogaban su alma. 
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
