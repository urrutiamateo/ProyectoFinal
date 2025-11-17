label creditos_finales:

    stop music fadeout 1.0
    scene black
    with fade

    # Velocidad del scroll
    $ credits_speed = 30  # menor = más lento

    # Texto de créditos
    $ creditos_texto = """
    {size=50}{b}CRÉDITOS{/b}{/size}
    
    {size=30}Game Desing:{/size}
    Mariela Gregnoli
    Rosalía Juárez
    
    {size=30}Producción:{/size}
    Yanina Tiribelli
    
    {size=30}Guión:{/size}
    Mariela Gregnoli
    Yanina Tiribelli
    Mateo Urrutia
    
    {size=30}Arte:{/size}
    Rosalía Juárez
    Yanina Tiribelli
    
    {size=30}Programación:{/size}
    Mariela Gregnoli
    Mateo Urrutia
    Yanina Tiribelli
    
    {size=30}Música:{/size}
    Maximiliano Ftulis
    Marcos Vallasciani
    
    {size=30}Agradecimientos:{/size}
    Maximiliano Ftulis
    Marcos Vallasciani
    Docentes de la UPSO
    y la UPSO
    
        """

    show text creditos_texto:
        xalign 0.5
        ypos 1.2   # inicia abajo de la pantalla
        linear credits_speed ypos -1.0  # sube hasta desaparecer

    with dissolve

    # Espera hasta que el scroll termine
    $ renpy.pause(credits_speed + 1)

    return
