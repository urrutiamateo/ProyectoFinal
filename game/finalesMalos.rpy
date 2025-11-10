label final_malo_ombu:
    scene viaje with fade
    play sound brisa

    narrator "Santos Vega se convirtió en el mejor payador, hechizaba a todos con su canto. Iba de pueblo en pueblo y a donde iba no quedaba nadie sin escucharlo."

    show santos_durmiendo_ombu
    "Una madrugada, mientras Santos Vega duerme entre viaje y viaje, en sus oscuros sueños oye unas voces."

    scene trono_mandinga with irisout

    voz_sueño1 "{color=#f5272e}{i}¿Qué desea el que me busca?{/i}{/color}"

    voz_sueño2 "{color=#F5D627}{i}Hechizar la pampa con mi canto.{/i}{/color}"

    voz_sueño1 "{color=#f5272e}{i}Pero eso cuesta... el alma. ¿Estás dispuesto…?{/i}{/color}"

    voz_sueño2 "{color=#F5D627}{i}¿Adónde hay que firmar?{/i}{/color}"

    scene contratoFirmado with fade

    narrator "Toda promesa tiene un precio. Y en sus sueños, Santos comenzó a pagarlo. Las voces no venían de afuera… sino de adentro. La pampa escuchó su canto, pero también su condena…"


    scene ombu with fade
    show santos_durmiendo_ombu
    
    "Una tarde Santos estaba descansando a la sombra de un Ombú, cuando de repente aparece un desconocido gaucho y se para delante de Santos."


    show juan_hablando at right
    juan "Despierta Santos. Veámos cuál de los dos es el mejor."

    menu:
        "¿Qué hará Santos?"
        "Mirar al gaucho y preguntarle su nombre":
            hide santos_durmiendo_ombu
            jump preguntarle
        "Ignorar al gaucho y seguir acostado sobre el ombú":
            jump ignorar
        
label preguntarle:
    hide juan_hablando
    show santos_neutro at left
    san "¿Quién se atreve a cortar mi sueño?"
    
    show juan_hablando at right
    juan "No soy hombre ni sombra, soy Juan Sin Ropa. Y vengo a cobrar una deuda de canto."

    jump ombu_final

label ignorar:
    show juan_hablando at right
    juan "Vamos, despierte, Santos. Levántese y agarre su guitarra. No puede escapar de mí, es su destino."
    hide santos_durmiendo_ombu
    jump ombu_final

label ombu_final:

    hide santos_neutro

    narrator "SANTOS VEGA Se levanta con su guitarra y empieza a cantar."

    show santos_payando at left

    call payada_ombu(musicPlaying=True)

    show santos_ojos_cerrados at left:
        zoom 0.5

    san "Estoy vencido."
    play sound brisa

    hide juan_guitarra with dissolve
    show serpiente at right

    narrator "Juan Sin Ropa se convierte en serpiente mientras el cuerpo de Santos se desvanece."

    hide santos_ojos_cerrados with dissolve

    narrator "El gaucho Santos Vega siempre será recordado como el gran cantor que recorrió las pampas y donde fue regalo las mejores payas."

    hide serpiente with dissolve
    
    narrator "Pero pocos saben que su canto también fue su condena."
    narrator "Dicen que aún se oye su voz en la llanura… no por gloria, sino por pena. Porque quien canta con el diablo nunca calla en paz."

    scene black
    "{size=80}FIN{/size}"