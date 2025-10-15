
default final_estado = ""

transform entrar_suave_izquierda:
    yalign 1.0
    xalign -0.5      
    linear 2.0 xalign 0.0 


# El juego comienza aquí.

label start:

    scene exteriorRanchoAtardecer

    "{color=#F5D627}{size=40}{b}SANTOS VEGA Y EL VIEJO DE LA PULPERIA{/b}{/size}{/color}"  

    with fade
    "En muchos lugares de la argentina se escucha hablar de la Salamanca, la cueva del Diablo donde brujos y alimanias bailan con las almas de los condenados.
    No es facil saber llegar, ni tampoco el entrar." 
    
    with dissolve
    "Pero quien lo logre, puede obtener dones extraordinarios, las mejores destrezas en el canto? 
    Solo si estas dispuesto a pagarlo...."
    
    scene exteriorRanchoNoche

    with fade
    "Otra dia que termina, en este pueblito pampero. 
    Santos encara hacia la pulperia.

    Va pensando: mis dotes no me alcanzan para ser el mejor guitarrero, 
    el mejor cantor, el mas habilidoso ni el mas famoso."

    scene exteriorPulperia

    with fade
    "Santos entra a la pulperia"

    scene interiorPulperia_2
    play music misterio volume 0.5 fadein 0.2

    with fade
    "La pulpería está llena de humo, guitarras y voces. Un viejo de mirada profunda murmura sobre la Salamanca."
    
    show viejo_neutro at right
    with dissolve
    viejo "... si se anima a agarrar viaje, porque llegar nomas ya es de valientes..."
    hide viejo_neutro

    show santos_neutro at left
    with dissolve
    "Santos Vega escucha, tentado por la ambición de ser el mejor cantor."

    with dissolve
    san "Buenas tardes.."

    show viejo_neutro at right 
    #with fade
    with dissolve
    viejo "Buenas tardes me dice usted, un gaucho mas del monton, sin fama ni encanto.
    No se crea que yo ando contando secretos a cualquier tirao."

    hide viejo_neutro
    hide santos_neutro

    scene interiorPulperia_1

    with fade
    "Santos se acerca a la barra y pide una caña"

    scene interiorPulperia_2

    show santos_neutro at left
    with dissolve
    san "Tome viejo, se lo manda el pulpero"

    show viejo_neutro at right
    with dissolve
    viejo "Sientese. Me llamo Don Ernesto, para empezar.."

    $ viejo = Character ("Don Ernesto")

    with dissolve
    viejo "pero no te puedo decir mas"

    with dissolve
    san "Lindo nombre, pero no me alcanza.
    
    Te escuche hablar sobre la Salamanca, y tenes pinta de saber pa donde queda."

    with dissolve
    viejo "Parece que a vos te falta un golpe de suerte, o algun milagro. Que te ponga de famoso o por lo menos bien parado."

    with fade
    "En la cueva del malo dentra uno mediocre, pero sale extraordinario.
    Alla podes probar tu temple, a ver si estas de corajudo lo suficiente."

    with dissolve
    "Pero hay que pensarlo con cuidado, se deja mucho por lo ganado.  
    Si estas dispuesto a ser otro por un dote, te canto el camino marcado."

    hide viejo_neutro

    hide santos_neutro

    menu:
        "¿Qué hace Santos?"

        "Ignorar la historia del viejo y quedarse en la pulpería tomando caña":
            jump payada_madiocre

        "Insistir al viejo para que le cuente el resto de la historia":
            stop music
            jump camino_a_salamanca

        

#Finales en la pulpería
label payada_madiocre:
    play music payada_intensa volume 0.5 fadein 0.5
    scene escena_pulperia_guitar
    # play music "pruebaSantosVega.mp3" volume 0.2
    with fade
    "Santos decide ignorar la leyenda. Se queda en la pulpería, improvisando payadas sin gloria."
    "Con el tiempo, se convierte en un cantor común, sin fama ni recuerdo duradero."

    call payada_manager(musicPlaying=True)

    with fade
    "Luego de ver que sus payadas no eran lo que el queria,
    Santos decide volver con el viejo para terminar de escuhcar la historia de la Salamanca"

    stop music
    jump camino_a_salamanca

    #menu:
        #"Resolver acertijo para volver al camino principal":
            #jump resolver_acertijo
    #return


label camino_a_salamanca: 
    scene None
    if humildad > ambicion:
        "tiene mas humildad que ambicion"
    elif humildad < ambicion:
        "tiene mas ambicion que humildad"
    else:
        "estan iguales"
        
    "aca comienza el segundo escenario"
    return






    

    

