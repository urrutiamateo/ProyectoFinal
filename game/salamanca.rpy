#ESCENA 2 EXTERIOR CUEVA ##############################################################################
label exterior_de_la_cueva:
    #show fondo_negro
    #with fade
   
    pause 0.5
    play music misterio volume 0.5 fadeout 2.0 fadein 1.0
    scene extCuevaCerrada with fade
    show santos_ext_cueva at center
    show caballo_cueva at right
    play sound sonido_caballo volume 0.5
    pause 2

    san "Tranquilo, tranquilo… De nerviosos está lleno el cementerio..."

    san "Ahora quedate piola acá y cuidame la guitarra."

    san "“Una piedra roja marca el camino”..."

label palabra_clave:

    san "¿Cuál era la palabra?"

    menu:
        "Cueva":
            $ subir_ambicion()
            # Bloque de código Python para hacer el logging
            $ print(f"DEBUG: La AMBICION actual es: {ambicion}")
            
            jump dentro_de_la_cueva

        "Sandía":
            "Vamos, ejercita un poco la memoria, Santos."
            $ subir_humildad()
            # Bloque de código Python para hacer el logging
            $ print(f"DEBUG: La HUMILDAD actual es: {humildad}")

            jump palabra_clave

            #dejamos payada mediocre comentado por si despues queremos hacer esa parte
            #jump payada_madiocre

label dentro_de_la_cueva:
    # SE ABRE LA CUEVA ##############################################################################
    
    scene extCuevaAbierta #with fade
    show santos_ext_cueva at center
    show caballo_cueva at right
    with dissolve
    play sound sonido_rocaCueva volume 1
    
    # se abre la cueva
    san "¡CUEVA!"
    "La entrada a la cueva de la Salamanca se abre con un resplandor rojizo."
    san "Que tanto..."

    "Santos ingresa a la cueva, dejando sus dudas atrás, por el momento..."

    hide santos_ext_cueva 
    #hide caballo_cueva 
    with dissolve 
    pause 1.0

    #ESCENA 4 INTERIOR CUEVA ###########################################################################
    scene intCueva with fade
    pause 0.5
    show santos_int_cueva at right


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

            python:
                subir_humildad()

            jump serpiente_enojada
        
            
        "“Aguantarse quieto ”":

            "Santos no se inmuta ante la prueba, sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."

            python:
                subir_ambicion()

            jump sale_serpiente

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

            python:
                subir_humildad()

            jump serpiente_enojada
        
            
        "“Aguantarse quieto”":
            "Santos no se inmuta ante la prueba, sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."
            
            python:
                subir_ambicion()

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
            "Santos quiere salir sorriendo, no resiste el terror que le provoca esta monstruosa cueva, pero ya no hay vuelta atrás..."

            python:
                subir_humildad()

            jump aparece_basilisco
            
        "“Cerrar los ojos”":
            "Santos cierra los ojos aguantando el temor que le provoca el basilisco, sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."

            python:
                subir_ambicion()

            jump desaparece_basilisco

    label desaparece_basilisco:
        # DESAPARECE BASILISCO ##############################################################################
        scene pantalla_negra with fade
        #play sound sound_heart volume 1 loop
        stop music fadeout 1.0
        play sound latidos_scare volume 1
        pause 30
        hide basilisco
        scene intCueva 
        show santos_int_cueva at right
        with fade
        #narrador
        stop sound
        #pause 0.5
        play sound suspiro_scare volume 0.5
        pause 12
        play music misterio volume 0.5 fadeout 2.0 fadein 1.0
        "La valentía es una virtud que pocos poseen. Santos demuestra tenerla y se aventura hacia lo más profundo de la demoníaca cueva."
        san "Muy bien, parece que eso funcionó..."

        san "Ahora tengo que elegir qué camino seguir.."
        menu:
            "“Cueva a la izquierda”":
                python:
                    subir_ambicion()

                jump cueva_equivocada2
            "“Cueva del centro”":

                python:
                    subir_ambicion()

                jump trono_mandinga
            "“Cueva a la derecha”":

                python:
                    subir_ambicion()

                jump cueva_equivocada1

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
            "“Cueva a la izquierda”":
                python:
                    subir_ambicion()

                jump cueva_equivocada2
            "“Cueva del centro”":
                python:
                    subir_ambicion()

                jump trono_mandinga
            "“Cueva a la derecha”":
                python:
                    subir_ambicion()
                jump cueva_equivocada1

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
            "“Cueva a la izquierda”":
                python:
                    subir_ambicion()

                jump cueva_equivocada2
            "“Cueva del centro”":
                python:
                    subir_ambicion()

                jump trono_mandinga
            "“Cueva a la derecha”":
                python:
                    subir_ambicion()

                jump cueva_equivocada1


    label trono_mandinga:
        # ESCENA  MANDINGA ##############################################################################
        scene trono_mandinga 
        play music musica_mandinga volume 0.5 fadeout 2.0 fadein 1.0
        show mandinga at center:
            zoom 0.8    
            xalign 0.4   
        show santos_int_cueva at right
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
        show santos_int_cueva at right
        with dissolve
        #play sound "risas_brujos.wav" volume 0.5
        "Un coro de brujos aparece entre las sombras. Sus risas retumban en la cueva, mezcladas con ecos y sonidos lejanos."

        diablo "Ellos serán testigos del pacto. ¡Elige, Santos Vega!"
        

        # Escena del contrato
        scene contrato with fade
        "El papel parece brillar con fuego. Santos observa el contrato... sus manos sudan y tiemblan."

        diablo "Solo una gota de tu sangre, y el don eterno del canto será tuyo. No te arrepentirás"

        san "El don del canto eterno... que todos conozcan mi nombre... ¡que tentador!"

        "En la mente de Santos resuena aquella frase de padrino... "
        "No hay canto más fuerte que el que nace del alma libre..."

        menu:
            "Firmar el contrato":
                python:
                    subir_ambicion()

                play sound carcajadasFinSalamanca volume 1
                "Santos firma sin dudarlo, lo que le ofrece el mandinga es todo lo que deseó siempre."
                scene contratoFirmado with dissolve
                diablo "Desde hoy, tu voz no conocerá silencio... Ni en tus sueños encontrarás silencio..."
                pause 10
                jump final_malo_ombu

            "Negarse a firmar":
                python:
                    subir_humildad()

                "Santos decide no firmar. El recuerdo de su padrino fue más fuerte que su ambición. Los brujos gritan, el fuego se apaga, y el Mandinga le grita con desprecio."
                scene trono_mandinga_2 with fade
                show mandinga at center:
                    zoom 0.8    
                    xalign 0.4   
                play sound carcajadasFinSalamanca volume 1
                pause 10

                diablo "Nadie rechaza al Mandinga sin pagar el precio..."
                pause 10
                "Santos corre lo más rápido que puede, saliendo de la cueva antes de que el Mandinga y sus brujos puedan alcanzarlo."
                
                jump final_bueno