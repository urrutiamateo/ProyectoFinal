
default final_estado = ""

transform entrar_suave_izquierda:
    yalign 1.0
    xalign -0.5      
    linear 2.0 xalign 0.0 


# El juego comienza aquí.

label start:

    scene exteriorRanchoAtardecer with irisout
    "{color=#F5D627}{size=40}{b}SANTOS VEGA Y EL VIEJO DE LA PULPERIA{/b}{/size}{/color}"  



    play music musica_intro volume 0.5 fadein 0.2
    # play music musica_intro volume 0.5 fadein 0.2
    with fade
    "En las llanuras abiertas de la pampa, cuando el sol se esconde detrás del horizonte y el viento lleva consigo ecos de antiguos cantares, vive un {b}jóven payador{/b} llamado {color=#F5D627}{b}Santos{/b}{/color}."
    with dissolve
    "Dicen que su voz puede calmar al caballo más bravo y que canta con la fuerza del que sueña, aunque le falta camino por andar antes de ganarse {b}un nombre y el brillo en su tierra{/b}."
    
    scene exteriorRanchoNoche
    with fade
    "Una noche, mientras las sombras cubren el campo, Santos siente el peso de su propio deseo: alcanzar la gloria, ser recordado, cantar como nadie lo ha hecho antes."

    show santos_espaldas at left
        #zoom 0.5
    with dissolve

    san "{i}Padre... {w=1.0}siempre dijiste que el alma libre es la que más canta.{/i}"
    san "{i}Pero a veces siento que mi voz no basta.\nQue hay algo allá lejos... {w=1.0}algo que me falta alcanzar para ser el más grande.{/i}"

    hide santos_espaldas
    with dissolve

    "El viento sopla y parece responderle con un susurro. En su mente, se enciende el recuerdo de una frase que su padrino le había dicho muchos años atrás."
    "{color=#F5D627}{b}{i}No hay canto más fuerte que el que nace del alma libre{/i}{/b}{/color}" #buscar recurso
    show santos_ojos_cerrados at left:
        zoom 0.5
    with dissolve
    "Santos cierra los ojos, sin saber que esa {b}frase{/b} será la última luz que lo guíe antes de que la oscuridad lo llame por su nombre."
    "Esa misma noche, atraído por el sonar de guitarras y voces lejanas, decide acercarse a la pulpería del pueblo..."
    hide santos_ojos_cerrados
    with dissolve
    scene exteriorPulperia
    with fade
    "Las risas y el murmullo de los hombres llegan hasta el camino. La pulpería brilla bajo la luna, iluminada por dentro con un farol cansado."
    
    show santos_a_caballo at right:
        alpha 0.7
        xzoom -1
        zoom 0.5
        linear 5 alpha 1.0

    with dissolve
    "Santos se detiene unos segundos, como si presintiera que al cruzar esa puerta {b}su vida ya no sería la misma{/b}."   
    #show santos_entero at left:
        #zoom 0.5
    #with dissolve
    "Respira hondo, salta del caballo, se acomoda la guitarra al hombro y decide entrar."
    hide santos_a_caballo
    with dissolve
    #stop music fadeout 2.0

    play music misterio volume 0.5 fadeout 2.0 fadein 2.0
    scene interiorPulperia_2
    with fade
    
    "El aire está espeso por el humo del tabaco. Gauchos beben, charlan y otros juegan a los naipes."
    show santos_entra_izquierda at left:
        linear 5 xpos 120
    with dissolve
    "Un {b}viejo{/b} de mirada extraña lo observa desde el fondo de una mesa mientras habla de la Salamanca, {b}{color=#a10000}la cueva donde dicen que el diablo concede dones{/color}{/b}."
    #show santos_neutro_iz at left:
        #xzoom -1
    #with dissolve
    "Santos lo escucha, {b}tentado por la ambición de ser el mejor cantor de la pampa{/b}."

    #show viejo_neutro at right:
        #zoom 0.9

    show viejo_en_la_pulperia
    with dissolve
    viejo "Dicen que tenés buena voz, muchacho... aunque todavía suena verde, como canto sin raíz."

    #show santos_neutro at left
    #with dissolve
    san "Y vos, viejo... {w=1.0}¿Qué sabés de voces y de raíces?"
    san "¿Qué podés saber de Salamancas?"
    viejo "Sé de muchas cosas, muchacho."
    viejo "La ubicación de ese lugar donde el {color=#a10000}Señor de la Salamanca{/color} da dones a los valientes, a los que sueñan en grande... {w=1.0}si están dispuestos a aceptar su {color=#a10000}pacto{/color}."


    hide viejo_en_la_pulperia 
    with dissolve
    hide santos_entra_izquierda
    with dissolve
    
    scene interiorPulperia_1
    with fade
    show santos_entero_sombra at center:
        alpha 0.8
        zoom 0.5
        linear 8 xpos 820 alpha 1.0
    with dissolve
    "Santos se acerca a la barra y pide una caña"
    "Él cree que con tragos el viejo le facilitará la {b}ubicación{/b} secreta"
    hide santos_entero_sombra
    with dissolve

    scene interiorPulperia_2
    with fade
    #show viejo_neutro at right:
        #zoom 0.9
    show viejo_en_la_pulperia 
    with dissolve
    #show santos_neutro_iz at left:
        #xzoom -1
    #with dissolve
    show santos_entra_izquierda at left:
        linear 5 xpos 120
    with dissolve

    san "Tome viejo, se lo manda el pulpero"
    san "Y...{w=0.5} pa' dónde dice que queda ese lugar?"

    viejo    "{i}La Salamanca está allá,{w=0.5}\ndonde la tierra ruge sin cesar,{w=0.5}\ny la luna en el cielo no se ve brillar,{w=0.5}\nquien allí vaya, secretos va a hallar.{w=0.5}{/i}"

    viejo "Tienes la {b}palabra secreta{/b}, muchacho."
    viejo "Pero hay que pensarlo con cuidado, se deja mucho por lo ganado"
    viejo "Pon tu guitarra al hombro, que no hay gloria para el que no la busca."

    
    hide viejo_en_la_pulperia 
    with dissolve
    san "Al diablo viejo charlatán !"
    "Santos se queda mirando con desconfianza. Pero las palabras del viejo suenan como un desafío que le quema por dentro."
    
    menu:
        "{size=40}¿Qué hace Santos?{/size}"

        "Ignorar la historia del viejo y quedarse en la pulpería tomando caña":
            jump payada_madiocre

        "Partir hacia la Salamanca":
            stop music
            jump camino_a_salamanca

        

#Finales en la pulpería
label payada_madiocre:
    play music payada_intensa volume 0.5 fadeout 2.0 fadein 2.0
    #play music payada_intensa volume 0.5 fadein 0.5
    scene interiorPulperia_2
    # play music "pruebaSantosVega.mp3" volume 0.2
    with fade
    show santos_payando at left
    with dissolve
    "Santos decide ignorar la leyenda. Se queda en la pulpería, improvisando payadas con los temas que pintan en el momento"
    "Es un cantor común, sin fama ni gloria."

    call payada_manager(musicPlaying=True)

    with fade
    "Luego de notar que sus payadas no superan la media del talento en su comunidad,
    Santos decide hacerle caso al viejo y {b}partir hacia la Salamanca{/b}"

    stop music
    jump camino_a_salamanca

    #menu:
        #"Resolver acertijo para volver al camino principal":
            #jump resolver_acertijo
    #return


label camino_a_salamanca: 
    scene viaje
    with fade
    if humildad > ambicion:
        "tiene más humildad que ambición"
    elif humildad < ambicion:
        "tiene más ambición que humildad"
    else:
        "están iguales"
        
    "camino hacia la Salamanca"
    return






    

    

