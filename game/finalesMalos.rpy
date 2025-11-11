label final_malo_ombu:
    scene viaje with fade
    play sound brisa volume 0.3 fadein 1.0 loop
    play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0

    narrator "Santos Vega se convirtió en el mejor payador, hechizaba a todos con su canto. Iba de pueblo en pueblo y a donde iba no quedaba nadie sin escucharlo."

    "Una madrugada, mientras Santos Vega duerme entre viaje y viaje, en sus oscuros sueños oye unas voces."

    stop sound fadeout 2.0

    show pantalla_gris:
        alpha 0.0
        linear 1.0 alpha 0.7  # sube opacidad a 0.5 en 1 segundo
    
    pause 1.5
    
    scene trono_mandinga with irisout
    
    hide pantalla_gris

    play music musica_mandinga volume 0.5 fadeout 2.0 fadein 1.0

    voz_sueño1 "{color=#f5272e}{i}¿Qué desea el que me busca?{/i}{/color}"

    voz_sueño2 "{color=#F5D627}{i}Hechizar la pampa con mi canto.{/i}{/color}"

    voz_sueño1 "{color=#f5272e}{i}Pero eso cuesta... el alma. ¿Estás dispuesto…?{/i}{/color}"

    voz_sueño2 "{color=#F5D627}{i}¿Adónde hay que firmar?{/i}{/color}"

    scene contratoFirmado with fade

    narrator "Toda promesa tiene un precio. Y en sus sueños, Santos comenzó a pagarlo. Las voces no venían de afuera… sino de adentro. La pampa escuchó su canto, pero también su condena…"

    show pantalla_roja:
        alpha 0.0
        linear 1 alpha 1  # sube opacidad a 0.7 en 1.5 segundos

    pause 1
    
    scene ombu with irisout

    hide pantalla_roja

    show santos_durmiendo_ombu
    play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0

    "Una tarde Santos estaba descansando a la sombra de un Ombú, cuando de repente aparece un desconocido gaucho y se para delante de Santos."

    show juan_hablando at right:
        zoom 1.25
    juan "Despierta Santos. Veámos cuál de los dos es el mejor."

    menu:
        "{space=350}{size=40}¿Qué hará Santos?{/size}"
        "Mirar al gaucho y preguntarle su nombre":
            hide santos_durmiendo_ombu with dissolve
            jump preguntarle
        "Ignorar al gaucho y seguir acostado sobre el ombú":
            jump ignorar
        
label preguntarle:
    hide juan_hablando with dissolve

    show santos_neutro at left with fade:
        zoom 0.75
    san "¿Quién se atreve a cortar mi sueño?"
    
    show juan_hablando at right:
        zoom 1.25
    juan "No soy hombre ni sombra, soy Juan Sin Ropa. Y vengo a cobrar una deuda de canto."
    hide santos_neutro with dissolve

    jump ombu_final

label ignorar:
    show juan_hablando at right:
        zoom 1.25
    juan "Vamos, despierte, Santos. Levántese y agarre su guitarra. No puede escapar de mí, es su destino."
    hide santos_durmiendo_ombu with dissolve
    jump ombu_final

label ombu_final:

    narrator "SANTOS VEGA Se levanta con su guitarra y empieza a cantar."

    show santos_payando at left with fade:
        zoom 0.75

    call payada_ombu(musicPlaying=True)

    show santos_ojos_cerrados at left:
        zoom 0.5

    san "Estoy vencido."

    hide juan_guitarra with dissolve

    show serpienteA at right
    
    play sound serpiente volume 0.3

    narrator "Juan Sin Ropa se convierte en serpiente mientras el cuerpo de Santos se desvanece."

    hide santos_ojos_cerrados with dissolve

    narrator "El gaucho Santos Vega siempre será recordado como el gran cantor que recorrió las pampas y donde fue regalo las mejores payas."

    hide serpienteA with dissolve
    
    narrator "Pero pocos saben que su canto también fue su condena."
    narrator "Dicen que aún se oye su voz en la llanura… no por gloria, sino por pena. Porque quien canta con el diablo nunca calla en paz."

    scene black
    show text "{size=80}FIN{/size}" at truecenter
    pause 3
    return