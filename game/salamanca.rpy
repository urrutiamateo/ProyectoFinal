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

    san "Shhh... Tranquilo, tranquilo… De nerviosos está lleno el cementerio..."

    san "Ahora quedate quietito acá y cuidame la guitarra."

    san "“Donde la tierra ruge”..."

    san "¡Ahí en la piedra roja!"

label palabra_clave:

    san "¿Cuál era la palabra?"

    menu:
        "Cueva":
            $ subir_ambicion()
            # Bloque de código Python para hacer el log
            $ print(f"DEBUG: La AMBICION actual es: {ambicion}")
            san "¡CUEVA!"
            jump dentro_de_la_cueva

        "Sandía":
            "Vamos, hace un poco de memoria, Santos."
            $ subir_humildad()
            # Bloque de código Python para hacer el log
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
    
    #"La entrada a la cueva de la Salamanca se abre con un resplandor rojizo."
    san "Qué tanto..."
    san "¡Pucha, qué olor a azufre!"
    

    #"Santos ingresa a la cueva, dejando sus dudas atrás, por el momento..."

    hide santos_ext_cueva 
    #hide caballo_cueva 
    with dissolve 
    pause 1.0

    #ESCENA 4 INTERIOR CUEVA ###########################################################################
    scene intCueva with fade
    pause 0.5
    show santos_int_cueva at right

    san "¡Pah..! Que olorcito a humedad y a tierra vieja... "

    san "Si se me llega a cruzar algún lagarto fiero, no traje nada pa' pegarle..."


    show serpienteA at center: 
        xzoom -1
    with dissolve

    play sound sfx_asustado
    show santos_int_cueva at salto_tiembla
    san "¡Que lo parió!"
    


    menu:
        "“Sacudirse las alimañas”":
            #"Santos se sacude algunos bichos..."

            python:
                subir_humildad()

            jump serpiente_enojada
        
            
        "“Aguantarse quieto ”":

            play sound alimanias_2
            
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
        show santos_int_cueva at saltito
        pause 1
        hide serpienteB
        show serpienteA at center: 
            xzoom -1
        with dissolve
        
        "Lo mejor ante las bestias, es permanecer inmóvil, y dejarlas que sigan por donde vinieron."
        san "¡Que lo parió! ¡No me quieren dejar tranquilo!"

    menu:
        "“Sacudirse las alimañas”":
            #"Santos se sacude algunos bichos ..."

            python:
                subir_humildad()
            jump serpiente_enojada
        
            
        "“Aguantarse quieto”":
            play sound alimanias_2
            
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
    "Santos sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."
    "Superó la primera prueba, pero el silencio dura poco." 
    "Algo más grande se arrastra en la oscuridad..."
    # APARECE BASILISCO ##############################################################################
    label aparece_basilisco:
    show basilisco at center 
    with dissolve
    play sound alimanias_1
    basilisco "¡QUIETO AHÍ!"
    basilisco "Si tu idea es ir más allá de esta penumbra, deberás tener el valor de mirarme a los ojos."
    
    menu:
        
        "“Huir del basilisco”":
            #"Santos quiere salir corriendo, no resiste el terror que le provoca esta monstruosa cueva, pero ya no hay vuelta atrás..."

            python:
                subir_humildad()

            jump aparece_basilisco
            
        "“Cerrar los ojos”":
            #"Santos cierra los ojos aguantando el temor que le provoca el basilisco, sabe lo que quiere, y aguanta cualquier cosa por la recompensa que le prometieron."
            
            
            python:
                subir_ambicion()

            jump desaparece_basilisco

    label desaparece_basilisco:
        # DESAPARECE BASILISCO ##############################################################################
        #scene pantalla_negra with fade
        
        
        stop music fadeout 1.0
        #play sound latidos_scare volume 1
        #play sound latidos_completo volume 1
        play sound sound_heart volume 1 loop
        
        
        #Aca se esconde el basilisco
        hide basilisco
        define fades = Fade(1,8,1)
        with fades
        # scene intCueva 
        # with fade(1,1,1)
        # pause 30

        # show santos_int_cueva at right
        # with dissolve
        #narrador
        # stop audio 
        stop sound fadeout 1.5

        #pause 0.5
        play sound suspiro_scare volume 0.5
        pause 5
        play music misterio volume 0.5 fadeout 2.0 fadein 1.0
        "La mirada de la bestia no encontró presa y regresó a la penumbra."
        san "¡Uff, se fue!... "
        san "Ni las bestias del infierno me van a frenar. Ahora... "
        san "¿Cuál de estas tres cuevas me lleva a lo del Mandinga?"

        play sound arpa_1 volume 1 fadeout 5.0
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

        san "¡La pucha...! Mejor por ahí no... me da mala espina."
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
        
        san "¡Que julepe! Mejor por ahí no voy."
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
        
        diablo "Has demostrado valentía, Santos Vega, o quizás inconsciencia."
        diablo "Tu alma atravesó el miedo, y tus pasos desafiaron lo prohibido. "
        diablo "Pocos hombres llegan hasta mi trono... y aún menos se van de aquí sin dejarme algo a cambio."

        san "¡Mandinga! Me trajo mi cuerpo, arrastrando el peso de una duda."
        san "¿Qué cosa desean los hombres, que se emparejan con tu deseo?"
        diablo "Ja! Todos queremos lo mismo.. fama, talento sin igual, el don de que nadie te supere jamás."

        san "¿Y a qué precio?"

        diablo "Toda ambición tiene su costo, cantor. ¡Firma!, y el mundo entero conocerá tu nombre."

        # Cambio de fondo: aparecen los brujos
        scene trono_mandinga_2 
        play sound risa_devil 
        show mandinga at center:
            zoom 0.8    
            xalign 0.4   
        show santos_int_cueva at right
        with dissolve
        #play sound "risas_brujos.wav" volume 0.5

        diablo "Ellos serán testigos del pacto. ¡Elige, Santos Vega!"
        

        # Escena del contrato
        scene contrato with fade
        
        diablo "Solo una gota de tu sangre, y el don eterno del canto será tuyo. No te arrepentirás"

        san "El don del canto eterno... que todos me conozcan... ¡Pucha!"
        san "Ya me puedo imaginar paseándome con mi renombre, la gloria acompañándome con mi guitarra. ¡Qué tentador!"

        "En la mente de Santos resuena aquella frase de padrino... "
        "No hay canto más fuerte que el que nace del alma libre..."

        menu:
            "Firmar el contrato":
                python:
                    subir_ambicion()

                play sound carcajadasFinSalamanca volume 1
                #"La sangre fresca y la ambición sellan el papel. No hubo duda en la mano, ni temblor en el trazo."
                scene contratoFirmado with dissolve
                diablo "¡Excelente elección, Santos Vega!"
                diablo "¡Bienvenido a mis huestes, desgraciado!"
                diablo "Desde hoy, tu voz no conocerá el silencio... Ni en tus sueños encontrarás la paz."
                pause 10
                
                # LÓGICA DE DECISIÓN DE FINALES
                # si la Humildad es mayor o igual a la Ambición, va al final del ombú.
                if humildad >= ambicion:
                    jump final_malo_ombu_2
    
                # si la Ambición es mayor que la humildad, va al final del incendio.
                else:
                    jump final_malo_incendio
                #jump final_malo_ombu

            "Negarse a firmar":
                python:
                    subir_humildad()

                scene trono_mandinga_2 with fade
                show mandinga at center:
                    zoom 0.8    
                    xalign 0.4   
                play sound carcajadasFinSalamanca volume 1
                pause 10

                diablo "Nadie rechaza al Mandinga sin pagar el precio..."
                diablo "¡Nadie se va de acá y vive para contarlo!"
                san "¡Yo me voy al mazo!"

                hide santos_int_cueva
                with dissolve
                pause 10
                
                
                jump final_bueno