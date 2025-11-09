
#default final_estado = ""
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
    #Position the karma display (e.g., top-right corner)
    #frame:
        #align (0.98, 0.02)  # Adjust alignment as needed
        #padding (10, 10)
        #text "Ambición: [ambicion]" size 24 color "#FFFFFF"  # Display the karma value
    #frame:
        ##padding (10, 10)
        #text "Ambición: [ambicion]" size 24 color "#FFFFFF"  # Display the karma value

# Add the screen to always be shown
init python:
    config.overlay_screens.append("karma_display")
    def subir_ambicion(cant:int=1):
        store.ambicion = getattr(store, 'ambicion', 0) + cant
    def subir_humildad(cant:int=1):
        store.humildad = getattr(store, 'humildad', 0) + cant

# El juego comienza aquí.
label start:

    scene exteriorRanchoAtardecer with irisout
    "{space=110}{cps=25}{color=#F5D627}{size=40}{b}SANTOS VEGA Y EL VIEJO DE LA PULPERIA{/b}{/size}{/color}"  
    play music musica_intro volume 0.5 fadein 0.2
    with fade
    "En las llanuras abiertas de la pampa, cuando el sol se esconde detrás del horizonte y el viento lleva consigo ecos de antiguos cantares, vive un {b}jóven payador{/b} llamado {color=#F5D627}{b}Santos{/b}{/color}."
    # dissolve
    "Dicen que su voz puede calmar al caballo más bravo y que canta con la fuerza del que sueña, aunque le falta camino por andar antes de ganarse {b}un nombre y el brillo en su tierra{/b}."
    #with dissolve
    scene exteriorRanchoNoche
    with fade
    "Una noche, mientras las sombras cubren el campo, Santos siente el peso de su propio deseo: alcanzar la gloria, ser recordado, cantar como nadie lo ha hecho antes."

    show santos_espaldas at left
        #zoom 0.5
    with dissolve

    san "{cps=20}{i}Padre... {w=0.5}siempre dijiste que el alma libre es la que más canta.{/i}"
    san "{cps=20}{i}Pero a veces siento que mi voz no basta.\nQue hay algo allá lejos... {w=0.5}algo que me falta alcanzar para ser el más grande.{/i}"

    hide santos_espaldas
    with dissolve
    play sound brisa

    "El viento sopla y parece responderle con un susurro. En su mente, se enciende el recuerdo de una frase que su padrino le había dicho muchos años atrás."
    "{space=60}{cps=20}{color=#F5D627}{b}{i}No hay canto más fuerte que el que nace del alma libre{/i}{/b}{/color}" #buscar recurso
    show santos_ojos_cerrados at left:
        zoom 0.5
    with dissolve
    "Santos cierra los ojos, sin saber que esa {b}frase{/b} será la última luz que lo guíe antes de que la oscuridad lo llame por su nombre."

#  Cambiaria la musica porque termina la introduccion y empieza la accion
    # play music misterio volume 0.5 fadeout 2.0 fadein 0.5

    hide santos_ojos_cerrados
    with dissolve
    "Esa misma noche, atraído por el sonar de guitarras y voces lejanas, decide acercarse a la pulpería del pueblo..."
    stop sound fadeout 2.0 
    

    scene exteriorPulperia
    with fade
    play sound murmullo volume 0.3 loop 
    "Las risas y el murmullo de los hombres llegan hasta el camino. La pulpería brilla bajo la luna, iluminada por dentro con un farol cansado."
    
    show santos_ext_pulperia at right

    with dissolve
    "Santos se detiene unos segundos, como si presintiera que al cruzar esa puerta {b}su vida ya no sería la misma{/b}."   
    #show santos_entero at left:
        #zoom 0.5
    #with dissolve
    "Respira hondo, salta del caballo, se acomoda la guitarra al hombro y decide entrar."
    hide santos_ext_pulperia
    with dissolve
    #pause 0.3
    #play sound puerta volume 0.3
    stop sound fadeout 2.0
    play music misterio volume 0.5 fadeout 2.0 fadein 1.0
    scene interiorPulperia_2
    with fade
    play sound puerta volume 0.3
    #pause 0.3
    #play sound murmullo volume 0.4  
    queue sound murmullo loop volume 0.2
    
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
    san "Y vos, viejo... {w=0.6}¿Qué sabés de voces y de raíces?"
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
        alpha 0.6
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
    show santos_con_cania at left:
        linear 4 xpos 130
    with dissolve

    san "Tome viejo, se lo manda el pulpero"
    san "Y...{w=0.5} pa' dónde dice que queda ese lugar?"
    hide viejo_en_la_pulperia
    with dissolve

    show viejo_hablando
    with dissolve

    viejo    "{cps=20}{i}La Salamanca está allá,{w=0.5}\ndonde la tierra ruge sin cesar,{w=0.6}\ny la luna en el cielo no se ve brillar,{w=0.6}\nquien allí vaya, secretos va a hallar.{w=0.6}{/i}"
    viejo "Tienes la {b}palabra secreta{/b}, muchacho."
    viejo "Pero hay que pensarlo con cuidado, se deja mucho por lo ganado"
    viejo "Pon tu guitarra al hombro, que no hay gloria para el que no la busca."

    hide santos_con_cania
    with dissolve
    hide viejo_hablando 
    with dissolve
    show santos_entra_izquierda at left:
        xpos 120
    san "Al diablo viejo charlatán !"
    "Santos se queda mirando con desconfianza. Pero las palabras del viejo suenan como un desafío que le quema por dentro."
    stop sound fadeout 2.0
    menu:
        "{space=350}{size=40}¿Qué hace Santos?{/size}"

        "Ignorar la historia del viejo y quedarse en la pulpería tomando caña":
            python:
                subir_humildad()
            jump payada_madiocre
            

        "Partir hacia la Salamanca":
            stop music
            python:
                subir_ambicion()
            jump camino_a_salamanca
            


label payada_madiocre:
    # play music payada_intensa volume 0.5 fadeout 2.0 fadein 2.0
    #play music payada_intensa volume 0.5 fadein 0.5
    scene interiorPulperia_2
    with fade
    # play music "pruebaSantosVega.mp3" volume 0.2
   
    show santos_payando at left
    with dissolve
    "Santos decide ignorar la leyenda. Se queda en la pulpería, improvisando payadas con los temas que pintan en el momento"
    "Es un cantor común, sin fama ni gloria."

    call payada_manager(musicPlaying=True)
    hide santos_payando
    hide payador_cantando
    #hide fondo_negro
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
#ESCENA 1 VIAJE A LA SALAMANCA ##############################################################################
    pause 0.5
    scene viaje with fade
    show santos_en_viaje at center
    play music musica_intro volume 0.5 fadeout 2.0 fadein 1.0
    play sound brisa volume 0.3

    "Santos abandona la pulpería en busca de la Salamanca, siguiendo las vagas indicaciones del Viejo."

    "En el campo abierto de la llanura, lo único que puede acompañar a Santos esa noche son seres vivientes que no hablan, pero igual dicen cosas."

    
    "Los insectos, su caballo, sus recuerdos, lo que lleva adentro.."

    "Después de horas de viaje, cruzar el río y el valle. Se ve más cerca la montaña, y en su ladera se vislumbran los males."

    "Santos investiga la falda rocosa, cuando de repente, su caballo se incomoda."

    "Los animales saben cuando algo anda mal."
    

#ESCENA 2 EXTERIOR CUEVA ##############################################################################
label exterior_de_la_cueva:
    #show fondo_negro
    #with fade
    pause 0.5
    play music misterio volume 0.5 fadeout 2.0 fadein 1.0
    scene extCuevaCerrada with fade
    show santos_ext_cueva at center
    show caballo_cueva at right
    

    san "Tranquilo, tranquilo… De nerviosos está lleno el cementerio.."

    san "Ahora quedate piola acá y cuidame la guitarra."

    san "“Una piedra roja marca el camino”..."

    san "¿Cuál era la palabra?"

    menu:
        "Cueva":
            
            jump dentro_de_la_cueva

        "Sandía":
            "El destino no quiso que Santos ingrese a la cueva. Quizás aún no esté listo para ponerse a prueba."
            san "Lo mejor será que vuelva, allá alguna canción me espera para burlar cualquier gaucho."
            jump payada_madiocre

label dentro_de_la_cueva:
    # SE ABRE LA CUEVA ##############################################################################
    
    scene extCuevaAbierta #with fade
    show santos_ext_cueva at center
    show caballo_cueva at right
    with dissolve
    
    # se abre la cueva
    san "“CUEVA”!"
    "La entrada a la cueva de la Salamanca se abre con un resplandor rojizo."
    san "Que tanto..."

    "Santos ingresa a la cueva, dejando sus dudas atrás, por el momento.."

    hide santos_ext_cueva 
    #hide caballo_cueva 
    with dissolve 
    pause 1.0

    #ESCENA 4 INTERIOR CUEVA ###########################################################################
    scene intCueva with fade
    pause 0.5
    show santos_ext_cueva at right


    "La cueva es sin dudas un lugar inhóspito..."
    san "Hay olor a pared con humedad, y a tierra vieja..."

    san "Y no me traje nada para cazar bichos..."

    #narrador
    "De repente, una cantidad de alimañas de todo tipo se trepan por el cuerpo de Santos, haciéndolo sudar en frío."

    show serpienteA at center: 
        xzoom -1
    with dissolve

    menu:
        "“Sacudirse las alimañas”":
            "Santos se sacude algunos bichos..."
            jump serpiente_enojada
        
            
        "“Aguantarse quieto ”":
            "Santos no se inmuta ante la prueba, sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."
            jump aparece_basilisco

    label serpiente_enojada:
        pause 0.5
        hide serpienteA
        show serpienteB at center: 
            xzoom -1
        with dissolve
        
        play sound serpiente
        
        pause 1
        hide serpienteB
        show serpienteA at center: 
            xzoom -1
        with dissolve
    #santos
    san "Al parecer eso las pone más agresivas."

    menu:
        "“Sacudirse las alimañas”":
            "Santos se sacude algunos bichos ..."
            jump serpiente_enojada
        
            
        "“Aguantarse quieto”":
            "Santos no se inmuta ante la prueba, sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."
            jump sale_serpiente

    #aparece basilisco
    label sale_serpiente:
    hide serpienteA
    show serpiente at left
    with dissolve
    pause 1
    hide serpiente
    with dissolve
    pause 0.5
    "La serpiente se retira huyendo, al ver que Santos no se inmuta."
    # APARECE BASILISCO ##############################################################################
    label aparece_basilisco:
    show basilisco at center 
    with dissolve
    basilisco "¡QUIETO AHÍ!"
    basilisco "Si tu idea es ir más allá de esta penumbra, deberás superar esta prueba."

    menu:
        "“Salir corriendo”":
            "Santos no resiste el terror que le provoca esta monstruosa cueva y sale corriendo..."
            jump exterior_de_la_cueva
            
        "“Cerrar los ojos”":
            "Santos cierra los ojos aguantando el temor que le provoca el basilisco, sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."
            jump desaparece_basilisco

    label desaparece_basilisco:
        # DESAPARECE BASILISCO ##############################################################################
        scene pantalla_negra with fade
        play sound sound_heart volume 0.5 loop
        pause 2.5
        hide basilisco
        scene intCueva 
        show santos_ext_cueva at right
        with fade
        #narrador
        "La valentía es una virtud que pocos poseen. Santos demuestra tenerla y se aventura hacia lo más profundo de la demoníaca cueva."
        san "Muy bien, parece que eso funcionó..."

        san "Ahora tengo que elegir qué camino seguir.."
        menu:
            "Cueva a la izquierda”":
                jump cueva_equivocada1
            "“Cueva del centro":
                jump trono_mandinga
            "“Cueva a la derecha”":
                jump aparece_basilisco#cueva_equivocada2

    label cueva_equivocada1:
        
        show murcielagos at truecenter
        with dissolve

        play sound sound_bat 

        pause 0.8
        hide murcielagos
        with dissolve
        "Un grupo de murciélagos salen volando y asustan a Santos."

        san "Mejor por ahí no... me da mala espina."
        menu:
            "Cueva del centro":
                jump trono_mandinga
            "Cueva a la derecha":
                jump cueva_equivocada2

    label cueva_equivocada2:
        
        show murcielagos at truecenter:
            xzoom -1
        with dissolve
        
        play sound sound_bat 

        pause 0.8
        hide murcielagos
        with dissolve
        "Un grupo de murciélagos salen volando y asustan a Santos."
        san "Que julepe! mejor por ahi no voy."
        menu:
            "Cueva a la izquierda”":
                jump cueva_equivocada1
            "“Cueva del centro":
                jump trono_mandinga


    label trono_mandinga:
        # ESCENA  MANDINGA ##############################################################################
        scene trono_mandinga 
        play music musica_mandinga volume 0.5 fadeout 2.0 fadein 1.0
        show mandinga at center:
            zoom 0.8    
            xalign 0.4   
        show santos_ext_cueva at right
        with fade
        
        diablo "Has demostrado ser digno, Santos Vega."
        diablo "Tu canto atravesó el miedo, y tus pasos desafiaron lo prohibido."
        diablo "Pocos hombres llegan hasta mi trono... y aún menos se van de aquí con vida."

        san "¿Y qué quiere usted, Mandinga?"

        diablo "Nada que no desees tú mismo... fama, talento sin igual, el don de que nadie te supere jamás."

        san "¿Y a qué precio?"

        diablo "Toda ambición tiene su costo, cantor. Solo una firma, y el mundo entero conocerá tu nombre."

        # Cambio de fondo: aparecen los brujos
        scene trono_mandinga_2 
        play sound risa_devil 
        show mandinga at center:
            zoom 0.8    
            xalign 0.4   
        show santos_ext_cueva at right
        with dissolve
        #play sound "risas_brujos.wav" volume 0.5
        "Un coro de brujos aparece entre las sombras. Sus risas retumban en la cueva, mezcladas con ecos y tambores lejanos."

        diablo "Ellos serán testigos del pacto. ¡Elige, Santos Vega!"
        

        # Escena del contrato
        scene contrato with fade
        "El papel parece brillar con fuego. Santos observa el contrato... sus manos sudan y tiemblan."

        diablo "Solo una gota de tu sangre, y el don eterno del canto será tuyo. No te arrepentirás"

        san "El don del canto eterno... que todos conozcan mi nombre... que tentador!."

        "En la mente de Santos resuena aquella frase de padrino... "
        "No hay canto más fuerte que el que nace del alma libre..."

        menu:
            "Firmar el contrato":
                "Santos firma sin dudarlo, lo que le ofrece el mandinga es todo lo que deseó siempre."
                scene contratoFirmado with dissolve
                diablo "Desde hoy, tu voz no conocerá silencio... Ni en tus sueños encontrarás silencio..."
                jump final_malo_ombu

            "Negarse a firmar":
                "Santos decide no firmar. El recuerdo de su padrino fue más fuerte que su ambición. Los brujos gritan, el fuego se apaga, y el Mandinga le grita con desprecio."
                scene trono_mandinga_2 with fade
                show mandinga at center:
                    zoom 0.8    
                    xalign 0.4   

                diablo "Nadie rechaza a Mandinga sin pagar el precio..."
                "Santos corre lo más rápido que puede, saliendo de la cueva antes de que el Mandinga y sus brujos puedan alcanzarlo."
                
                jump final_bueno



        



    #jump finales_malos_Yani
    return

    






    

    

