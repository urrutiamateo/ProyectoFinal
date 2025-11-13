transform scroll_credits:
    ypos 1080  # empieza justo debajo de la pantalla
    linear 50.0 ypos -5500  # termina arriba

label creditos:

    scene black
    play music "feliz.mp3"
    show screen creditscreen
    pause 30 # tiempo total de desplazamiento
    hide screen creditscreen
    stop music fadeout 3.0
    scene black with fade
    return

screen creditscreen:
    frame:
        background None
        xalign 0.5
        yalign 0.0
        has vbox
        vbox:
            spacing 25
            at scroll_credits
            text "SANTOS VEGA Y EL VIEJO DE LA PULPERIA":
                size 60
                color "#F5D627"
                xalign 0.5
            text "PAMPA GAME":
                bold True
                size 60
                color "#a36f34"
                outlines [(1, "#5a2007")]
                xalign 0.5
            text "Créditos":
                size 45
                color "#FFFFFF"
                xalign 0.5
            # ARTE
            text "Arte:":
                size 40
                bold True
                xalign 0.5
            text "Rosa Juarez\nYanina Tiribelli":
                size 35
                xalign 0.5
            # GUION
            text "Guión:":
                size 40
                bold True
                xalign 0.5
            text "Mariela Gregnoli\nYanina Tiribelli\nMateo Urrutia ":     
                size 35
                xalign 0.5
            # GAME DESIGNER
            text "Game Designer:":          
                size 40
                bold True
                xalign 0.5
            text "Mariela Gregnoli\nRosa Juarez\nYanina Tiribelli":               
                size 35
                xalign 0.5
            # MUSICA
            text "Música:":           
                size 40
                bold True
                xalign 0.5
            text "Marcos Vallasciani\nMaximiliano Ftulis":            
                size 35
                xalign 0.5
            text "Producción:":         
                size 40
                bold True
                xalign 0.5
            text "Yanina Tiribelli":
                size 35
                xalign 0.5
            # PROGRAMACION
            text "Programación:":        
                size 40
                bold True
                xalign 0.5
            text "Mariela Gregnoli\nMateo Urrutia":          
                size 35
                xalign 0.5

            # AGRADECIMIENTOS
            text "Agradecimientos:":
                size 40
                bold True
                xalign 0.5
            text "- Al compañero Marcos Vallasciani\n- A la inspiración y al mate de medianoche\n":   
                size 35
                xalign 0.5
            text "Dedicatoria:":
                size 30
                bold True
                xalign 0.5
            text "A mi querida madre, cuya luz y amor por la tradición gaucha sigue iluminando cada rincón de este juego.":
                size 30
                xalign 0.5

            vbox:
                ysize 150 

            text "Gracias por jugar ♥":
                size 50
                color "#e52d4c"
                xalign 0.5

