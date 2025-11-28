
transform entrar_suave_izquierda:
    yalign 1.0
    xalign -0.5      
    linear 2.0 xalign 0.0 

screen karma_display():
    frame:       
        align (0.98, 0.05)
        background Frame("gui/FondoJuego.jpg", 10, 10)
        padding(10, 10, 20, 10)  
        vbox:
            spacing 6
            text "Humildad: [humildad]" size 24 color "#FFFFFF" outlines [(2, "#5a2007")] # Display the karma value
            text "Ambición: [ambicion]" size 24 color "#FFFFFF" outlines [(2, "#5a2007")] # Display the karma value
    
init python:
    config.overlay_screens.append("karma_display")
    def subir_ambicion(cant:int=1):
        store.ambicion = getattr(store, 'ambicion', 0) + cant
    def subir_humildad(cant:int=1):
        store.humildad = getattr(store, 'humildad', 0) + cant
    #CLASE PERSONAJE
    #from python.personajes.personajes import SantosVega, ViejoPulperia
    #san = SantosVega(p_san)
    #viejo = ViejoPulperia(p_viejo)


# El juego comienza aquí.
label start:
    #CLASE PERSONAJE
    #$ san.personalizado = p_san
    #$ viejo.personalizado = p_viejo

    stop music fadeout 0.5
    play music musica_intro fadein 0.2 volume 0.7
    scene exteriorRanchoAtardecer with irisout
    "{space=110}{cps=25}{color=#F5D627}{size=40}{b}SANTOS VEGA Y EL VIEJO DE LA PULPERIA{/b}{/size}{/color}"  
    # play music musica_intro fadein 0.2
    with fade
    "En las llanuras abiertas de la pampa vive un {b}jóven payador{/b} llamado {color=#F5D627}{b}Santos{/b}{/color}."
    # dissolve
    "Dicen que su voz puede calmar al caballo más bravo y que canta con la fuerza del que sueña, aunque le falta camino por andar antes de {b}ganarse un nombre y el brillo en su tierra{/b}."
    #with dissolve
    scene exteriorRanchoNoche
    with fade
    "Santos siente el peso de su propio deseo: alcanzar la gloria y cantar como nadie lo ha hecho antes."

    show santos_espaldas at left
        #zoom 0.5
    with dissolve
    san "{cps=20}{i}Padre... {w=0.5}siempre dijiste que el alma libre es la que más canta.{/i}"
    san "{cps=20}{i}Pero a veces siento que mi voz no basta.\nQue hay algo allá lejos... {w=0.5}algo que me falta alcanzar para ser el más grande.{/i}"
    
    #CLASE PERSONAJE
    #$ san.hablar("{cps=20}{i}Padre... {w=0.5}siempre dijiste que el alma libre es la que más canta.{/i}")
    #$ san.hablar("{cps=20}{i}Pero a veces siento que mi voz no basta.\nQue hay algo allá lejos... {w=0.5}algo que me falta alcanzar para ser el más grande.{/i}")

    hide santos_espaldas
    with dissolve
    play sound brisa fadein 1

    "El viento parece responderle con un susurro. En su mente, se enciende el recuerdo de una frase que le había dicho su padre."
    show santos_ojos_cerrados at left:
        zoom 0.5
    with dissolve
    "{space=60}{cps=20}{color=#F5D627}{b}{i}No hay canto más fuerte que el que nace del alma libre{/i}{/b}{/color}" #buscar recurso
    
    #"Santos cierra los ojos, sin saber que esa {b}frase{/b} será la última luz que lo guíe antes de que la oscuridad lo llame por su nombre."

#  Cambiaria la musica porque termina la introduccion y empieza la accion
    # play music misterio volume 0.5 fadeout 2.0 fadein 0.5

    hide santos_ojos_cerrados
    with dissolve
    #"Esa misma noche, atraído por el sonar de guitarras y voces lejanas, decide acercarse a la pulpería del pueblo..."
    
    stop sound fadeout 2.0 
    

    scene exteriorPulperia
    with fade
    play sound murmullo volume 0.2 loop fadein 2
    #"Las risas y el murmullo de los hombres llegan hasta el camino. La pulpería brilla bajo la luna, iluminada por dentro con un farol cansado."
    "Esa misma noche el murmullo de la pulpería lo invita a acercarse."
    show santos_ext_pulperia at right

    with dissolve
    #"Santos se detiene unos segundos, como si presintiera que al cruzar esa puerta {b}su vida ya no sería la misma{/b}."   
    #show santos_entero at left:
        #zoom 0.5
    #with dissolve
    #"Santos salta del caballo, se acomoda la guitarra al hombro y decide entrar."
    play sound sonido_caballo volume 0.3
    san "Si quiero que mi voz llegue a toda la pampa, tengo que empezar por algún lado..."
    hide santos_ext_pulperia
    with dissolve
    stop music fadeout 1.0
    #pause 0.3
    #play sound puerta volume 0.3
    stop sound fadeout 1.0
    play music misterio fadeout 2.0 fadein 2.0
    scene interiorPulperia_2
    with fade
    play sound puerta volume 0.3
    queue sound murmullo volume 0.2 loop
    #pause 0.3 
    show santos_entra_izquierda at left:
        linear 5 xpos 120
    with dissolve
    #pause 0.3
    #play sound murmullo volume 0.4  
    
    
    san "Pucha que está espeso. Especial para una ronda de caña y cartas.\nA ver si esta noche pinta la buena racha."
    
    "Un {b}viejo{/b} de mirada extraña lo observa desde el fondo de una mesa mientras habla de la Salamanca, {b}{color=#a10000}la cueva donde dicen que el diablo concede dones{/color}{/b}."
    #show santos_neutro_iz at left:
        #xzoom -1
    #with dissolve
    #"Santos lo escucha, {b}tentado por la ambición de ser el mejor cantor de la pampa{/b}."

    #show viejo_neutro at right:
        #zoom 0.9

    show viejo_en_la_pulperia
    with dissolve
    viejo "Dicen que tenés buena voz, muchacho... aunque todavía suena verde, como canto sin raíz."
    #viejo "Dicen que tenés buena voz, muchacho... aunque todavía suena verde, como canto sin raíz."

    #show santos_neutro at left
    #with dissolve
    san "Y vos, viejo... {w=0.6}¿Qué sabés de voces y de raíces?"
    san "¿Qué podés saber de la Salamanca?"
    viejo "Sé de muchas cosas, muchacho."
    viejo "La ubicación de ese lugar donde el {b}{color=#a10000}Señor de la Salamanca{/color}{/b} da dones a los valientes, a los que sueñan en grande... {w=1.0}si están dispuestos a aceptar su {b}{color=#a10000}pacto{/color}{/b}."

    hide viejo_en_la_pulperia 
    with dissolve
    hide santos_entra_izquierda
    with dissolve
    
    scene interiorPulperia_1
    with fade
    show santos_entero_sombra at center:
        #alpha 0.6
        zoom 0.5
        linear 6 xpos 820 #alpha 1.0
    with dissolve
    san "Andá a saber cuánto hace que ese viejo anda dando vueltas por acá."
    san "Si le llevo un trago capaz que afloja la lengua.\nEstos viejos saben más de lo que dicen. Y cuando hablan, nunca es de gusto."
    

    

    #"Santos se acerca a la barra y pide una caña."
#"Él cree que con tragos el viejo le facilitará la {b}ubicación{/b} secreta."
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
    show santos_con_cania at left:
        linear 4 xpos 130
    with dissolve

    san "Tome viejo, se lo manda el pulpero"
    san "Y...{w=0.5} ¿Pa' dónde dice que queda ese lugar?"
    hide viejo_en_la_pulperia
    with dissolve

    show viejo_hablando
    with dissolve

    viejo "{cps=20}{i}La Salamanca está allá,{w=0.5}\ndonde la tierra ruge sin cesar,{w=0.6}\ny la luna en el cielo no se ve brillar,{w=0.6}\nquien allí vaya, secretos va a hallar.{w=0.6}{/i}"
    viejo "Tienes la {b}palabra secreta{/b}, muchacho."
    viejo "Pero hay que pensarlo con cuidado, se deja mucho por lo ganado."
    viejo "Pon tu guitarra al hombro, que no hay gloria para el que no la busca."

    hide santos_con_cania
    with dissolve
    hide viejo_hablando 
    with dissolve
    show santos_entra_izquierda at left:
        xpos 120
    san "¡Al diablo, viejo charlatán!"
    #"Santos se queda mirando con desconfianza. Pero las palabras del viejo suenan como un desafío que le quema por dentro."
    stop sound fadeout 5.0
    menu:
        "{space=350}{size=40}¿Qué hace Santos?{/size}"

        "Ignorar la historia del viejo y quedarse en la pulpería":
            
            python:
                subir_humildad()
            jump payada_madiocre
            

        "Partir hacia la Salamanca":
            stop music fadeout 2.0
            python:
                subir_ambicion()
            jump camino_a_salamanca
            


label payada_madiocre:
    # play music payada_intensa volume 0.5 fadeout 2.0 fadein 2.0
    #play music payada_intensa volume 0.5 fadein 0.5
    scene interiorPulperia_2
    with fade
    # play music "pruebaSantosVega.mp3" volume 0.2
   
    show santos_entra_izquierda at left
    with dissolve

    san "Gaucho... ¿Se presta para una guitarreada?"

    show rival_payador at right:
        zoom 1.2
        align (0.6, -0.3)
    with dissolve
    payador "Para eso venimos, compadre."

    stop music fadeout 2.0
    hide santos_entra_izquierda
    hide rival_payador 
    with fade

    # "Santos decide ignorar la leyenda. Se queda en la pulpería, improvisando payadas con los temas que pintan en el momento."
    #"Es un cantor común, sin fama ni gloria."

    call payada_manager(musicPlaying=True) from _call_payada_manager
    hide santos_payando
    hide payador_cantando
    #hide fondo_negro
    with fade
    # "Luego de notar que sus payadas no superan la media del talento en su comunidad,
    # Santos decide hacerle caso al viejo y {b}partir hacia la Salamanca{/b}"

    stop music fadeout 2.0

    jump camino_a_salamanca
    #menu:
        #"Resolver acertijo para volver al camino principal":
            #jump resolver_acertijo
    #return



label camino_a_salamanca: 
#ESCENA 1 VIAJE A LA SALAMANCA ##############################################################################
    # pause 0.5
    scene viaje with fade
    show santos_en_viaje at center
    play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0
    play sound brisa volume 0.3

    "Santos abandona la pulpería en busca de la Salamanca, siguiendo las vagas indicaciones del Viejo."

    "En el campo abierto de la llanura, lo único que puede acompañar a Santos esa noche son seres vivientes que no hablan, pero igual dicen cosas."

    
    "Los insectos, su caballo, sus recuerdos, lo que lleva adentro..."

    "Después de horas de viaje, cruzar el río y el valle. Se ve más cerca la montaña, y en su ladera se vislumbran los males."

    "Santos investiga la falda rocosa, cuando de repente, su caballo se incomoda."

    "Los animales saben cuando algo anda mal."

    jump exterior_de_la_cueva
    





        



    
    

    






    

    

