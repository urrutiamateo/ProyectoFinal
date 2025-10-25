
default final_estado = ""

transform entrar_suave_izquierda:
    yalign 1.0
    xalign -0.5      
    linear 2.0 xalign 0.0 


# El juego comienza aquí.

label start:

    scene exteriorRanchoAtardecer

    "{color=#F5D627}{size=40}{b}SANTOS VEGA Y EL VIEJO DE LA PULPERIA{/b}{/size}{/color}"  
    play music misterio volume 0.5 fadein 0.2
    # play music musica_intro volume 0.5 fadein 0.2



    with fade
    "En las llanuras abiertas de la pampa, cuando el sol se esconde detrás del horizonte y el viento lleva consigo ecos de antiguos cantares, vive un jóven payador llamado Santos."
    with dissolve
    "Dicen que su voz puede calmar al caballo más bravo y que canta con la fuerza del que sueña, aunque le falta camino por andar antes de ganarse un nombre y el brillo en su tierra."
    
    scene exteriorRanchoNoche
    with fade
    "Esa noche, mientras las sombras cubren el campo, Santos siente el peso de su propio deseo: alcanzar la gloria, ser recordado, cantar como nadie lo ha hecho antes."

    show santos_espaldas at left
        #zoom 0.5
    with dissolve

    san "Padre... siempre dijiste que el alma libre es la que más canta."
    san "Pero a veces siento que mi voz no basta. Que hay algo allá lejos... algo que me falta descubrir."

    hide santos_espaldas
    with dissolve

    "El viento sopla y parece responderle con un susurro. En su mente, se enciende el recuerdo de una frase que su padre le había dicho muchos años atrás."
    "No hay canto más fuerte que el que nace del alma libre." #buscar recurso
    show santos_ojos_cerrados at left:
        zoom 0.5
    with dissolve
    "Santos cierra los ojos, sin saber que esa frase será la última luz que lo guíe antes de que la oscuridad lo llame por su nombre."
    "Esa misma noche, atraído por el rumor de guitarras y voces lejanas, decide acercarse a la pulpería del pueblo..."
    hide santos_ojos_cerrados
    with dissolve
    scene exteriorPulperia
    with fade
    "Las risas y el murmullo de los hombres llegan hasta el camino. La pulpería brilla bajo la luna, iluminada por dentro con un farol cansado."
    
    show santos_a_caballo at right:
        xzoom -1
        zoom 0.55

    with dissolve
    "Santos se detiene unos segundos, como si presintiera que al cruzar esa puerta su vida ya no sería la misma."   
    #show santos_entero at left:
        #zoom 0.5
    #with dissolve
    "Respira hondo, se acomoda la guitarra al hombro y decide entrar."
    hide santos_a_caballo
    with dissolve


    scene interiorPulperia_2
    with fade
    "El aire está espeso por el humo del tabaco. Gauchos beben, otros juegan a los naipes."
    show santos_entra_izquierda at left:
        linear 5 xpos 120
    with dissolve
    "Un viejo de mirada extraña lo observa desde el fondo de una mesa mientras habla de la Salamanca, la cueva donde dicen que el diablo concede dones."
    #show santos_neutro_iz at left:
        #xzoom -1
    #with dissolve
    "Santos Vega escucha, tentado por la ambición de ser el mejor cantor."

    show viejo_neutro at right:
        zoom 0.9
    with dissolve
    viejo "Dicen que tenés buena voz, muchacho... aunque todavía suena verde, como canto sin raíz."

    #show santos_neutro at left
    with dissolve
    san "Y vos, viejo... ¿Qué sabés de voces y de raíces?"
    san "¿Qué podés saber de Salamancas?"
    viejo "Sé de muchas cosas, muchacho."
    viejo "La ubicación de ese lugar donde el Señor de la Salamanca da dones a los valientes... si están dispuestos a aceptar su pacto."


    hide viejo_neutro
    with dissolve
    hide santos_neutro_iz
    with dissolve
    
    scene interiorPulperia_1
    with fade
    show santos_entero_sombra at center:
        zoom 0.5
        linear 6 xpos 820
    with dissolve
    "Santos se acerca a la barra y pide una caña"
    "Él cree que con tragos el viejo le facilitará la ubicación secreta"
    hide santos_entero_sombra
    with dissolve

    scene interiorPulperia_2
    with fade
    show viejo_neutro at right:
        zoom 0.9
    with dissolve
    #show santos_neutro_iz at left:
        #xzoom -1
    #with dissolve
    show santos_entra_izquierda at left:
        linear 5 xpos 120
    with dissolve
    san "Tome viejo, se lo manda el pulpero"
    san "Y 'pa dónde queda ese lugar?"

    viejo   "La Salamanca está allá, {w=0.3} \n
            donde la tierra ruge sin cesar,{w=0.3} \n
            y la luna en el cielo no se ve brillar,{w=0.3} \n
            quien allí vaya, secretos va a hallar.{w=0.3}"

    viejo "Tienes la palabra secreta, muchacho."
    viejo "Pero hay que pensarlo con cuidado, se deja mucho por lo ganado"
    viejo "Pon tu guitarra al hombro, que no hay gloria para el que no la busca."

    
    hide viejo_neutro
    with dissolve

    "Santos se queda mirando con desconfianza. Pero las palabras del viejo suenan como un desafío que le quema por dentro."
    "Al diablo viejo charlatán"
    

    menu:
        "¿Qué hace Santos?"

        "Ignorar la historia del viejo y quedarse en la pulpería tomando caña":
            jump payada_madiocre

        "Partir hacia la Salamanca":
            stop music
            jump camino_a_salamanca

        

#Finales en la pulpería
label payada_madiocre:
    play music payada_intensa volume 0.5 fadein 0.5
    scene escena_pulperia_guitar
    # play music "pruebaSantosVega.mp3" volume 0.2
    with fade
    "Santos decide ignorar la leyenda. Se queda en la pulpería, improvisando payadas con los temas que pintan en el momento"
    "Es un cantor común, sin fama ni gloria."

    call payada_manager(musicPlaying=True)

    with fade
    "Luego de notar que sus payadas no superan la media del talento en su comunidad,
    Santos decide hacerle caso al viejo y partir hacia la Salamanca"

    stop music
    jump camino_a_salamanca

    #menu:
        #"Resolver acertijo para volver al camino principal":
            #jump resolver_acertijo
    #return


label camino_a_salamanca: 
    scene None
    if humildad > ambicion:
        "tiene más humildad que ambición"
    elif humildad < ambicion:
        "tiene más ambición que humildad"
    else:
        "están iguales"
        
    "acá comienza el segundo escenario"
    return






    

    

