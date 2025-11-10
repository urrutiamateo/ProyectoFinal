define san = Character("Santos Vega", color = "#d6b707")
#define p_san = Character("Santos Vega", color = "#d6b707")   #PARA CLASE PERSONAJE
define viejo = Character("Don Ernesto", color= "#b81c07")
#define p_viejo = Character("Don Ernesto", color= "#b81c07")     #PARA CLASE PERSONAJE
define diablo = Character("Mandinga")
define payador = Character("Payador del Pueblo", color = "#0abe79")  
define narrator = Character(None)
define basilisco = Character("Basilisco")
define juan = Character("Juan Sin Ropa", color= "#b81c07")
define voz_sueño1 = Character(None)
define voz_sueño2 = Character(None)
#$ titulo_texto = "{color=#F5D627}{size=40}{b}SANTOS VEGA Y EL VIEJO DE LA PULPERIA{/b}{/size}{/color}"
#define Titulo = Character("{color=#F5D627}{size=40}{b}SANTOS VEGA Y EL VIEJO DE LA PULPERIA{/b}{/size}{/color}", window_text_align=0.5)


image santos_entero_sombra = "images/sprites/Santos_conSombra.png"
image santos_neutro_ = "images/sprites/santos_entero_iz.png"
image santos_espaldas = "images/sprites/Santos_espaldas_conSombra.png"
image santos_neutro = "images/sprites/santos_medio_cuerpo.png"
image santos_asombrado = "images/sprites/santos_asombrado_s.png"
image santos_asustado = "images/sprites/santos_asustado_s.png"
image santos_ojos_cerrados = "images/sprites/Santos_ojos_cerrados_conSombra.png"
image santos_a_caballo = "images/sprites/sv montado.png"
image santos_ext_pulperia = "images/sprites/Santos_ExteriorPulperia.png"
image santos_entra_izquierda = "images/sprites/Santos_para_interiorPulperia_2.png"
image santos_con_cania = "images/sprites/Santos_Cania_en_interiorPulperia.png"
image santos_payando = "images/sprites/Santos_guitarra_en_interiorPulperia.png"
image santos_en_viaje = "images/sprites/Santos_en_viaje.png"
image santos_ext_cueva = "images/sprites/Santos_en_extCueva.png"

# Sprites de salamanca
image caballo_cueva = "images/sprites/caballo_en_extCueva.png"
image basilisco = "images/sprites/basilisco.png"
image serpiente = "images/sprites/Serpiente1_intCueva.png"
image serpienteA = "images/sprites/Serpiente2_intCueva_a.png"
image serpienteB = "images/sprites/Serpiente2_intCueva_b.png"
image mandinga = "images/sprites/mandinga.png"

image viejo_en_la_pulperia = "images/sprites/Viejo_en_interiorPulperia.png"
image viejo_neutro_ = "images/sprites/viejo_neutro.png"
image viejo_neutro = "images/sprites/viejo_neutro_s.png"
image viejo_malo = "images/sprites/viejo_malo_s.png"
image viejo_hablando = "images/sprites/viejo de la pulperia de pie hablando.png"

image rival_payador = "images/sprites/Payador_2_en_interiorPulperia_2.png"
image payador_cantando = "images/sprites/Payador_guitarra_en_interiorPulperia_2.png"


image pulperiaGuitarra = "images/fondos/escena_pulperia_guitar.png"
image exteriorRanchoAtardecer = "images/fondos/exteriorRanchoAtardecer.jpg"
image exteriorRanchoNoche = "images/fondos/exteriorRanchoNoche1.jpg"
image exteriorPulperia = "images/fondos/ExteriorPulperia.jpg"
image interiorPulperia_1 = "images/fondos/interiorPulperia_1.jpg"
image interiorPulperia_2 = "images/fondos/interiorPulperia_2.jpg"
image viaje = "images/fondos/viaje.jpg"
image extCuevaCerrada = "images/fondos/extCuevaCerrada.jpg"
image extCuevaAbierta = "images/fondos/extCuevaAbierta.jpg"
image intCueva = "images/fondos/intCueva.jpg"
image contrato = "images/fondos/PlanoContrato.jpg"
image contratoFirmado = "images/fondos/PlanoContratoFirmado.jpg"
image trono_mandinga = "images/fondos/Trono_Sr_m_v2.jpg"
image trono_mandinga_2 = "images/fondos/Trono_Sr_m_v3.jpg"

# sprites ombu
image juan_hablando = "images/sprites/JuanSinRopa_hablando.png"
image juan_guitarra = "images/sprites/JuanSinRopa_guitarra.png"
image santos_durmiendo_ombu = "images/sprites/Santos_dormido_ombu.png"

image ombu = "images/fondos/ombu_conSombraSantosDurmiendo.png"

# Un filtro negro semitransparente
image fondo_negro = Solid("#00000083")
image pantalla_negra = Solid ("#000000ff")
define slowfade = Fade(2.0, 0.0, 2.0)

define fin_payada_intensa = "audio/finpayadaintensa.mp3"
define payada_intensa = "audio/payadaintensa.mp3"
define payada_feliz = "audio/payadaalegre.mp3"
define misterio = "audio/misterio.mp3"
define musica_intro = "audio/Nuevos/Santos Vega_Musica_Intro.mp3"
define musica_mandinga = "audio/Nuevos/Cueva_Mandinga.mp3"

define paya_1_A = "audio/Nuevos/Primer_Paya/Paya_Frase_1.ogg"
define paya_1_B = "audio/Nuevos/Primer_Paya/Paya_Frase_2.ogg"
define paya_1_final = "audio/Nuevos/Primer_Paya/Paya_FinalCorte.ogg"
define paya_1_enganche = "audio/Nuevos/Primer_Paya/Paya_FinalConEnganche.mp3"
define paya_1_AyB = "audio/Nuevos/Primer_Paya/Paya_completa_loop.mp3"
define brisa = "audio/Sonidos/brisa.mp3"
define puerta = "audio/Sonidos/puerta.mp3"
define sound_bat = "audio/Sonidos/murcielagos_flapping-sound.wav"
define sound_heart_loop= "audio/Sonidos/heartbeat-loop.wav"
define sound_heart = "audio/Sonidos/heartbeats-imperfections.wav"
define serpiente = "audio/Sonidos/serpiente.wav"
define risa_devil= "audio/Sonidos/flail-demon-laugh.wav"
define aplausos = "audio/Sonidos/aplausos__shagger.wav"

#animacion murcielagos
image murcielagos = Animation(
    "images/frames/murcielagos_0001.png", 0.033,
    "images/frames/murcielagos_0003.png", 0.033,
    "images/frames/murcielagos_0002.png", 0.033,
    "images/frames/murcielagos_0004.png", 0.033,
    "images/frames/murcielagos_0005.png", 0.033,
    "images/frames/murcielagos_0006.png", 0.033,
    "images/frames/murcielagos_0007.png", 0.033,
    "images/frames/murcielagos_0008.png", 0.033,
    "images/frames/murcielagos_0009.png", 0.033,
    "images/frames/murcielagos_0010.png", 0.033,
    "images/frames/murcielagos_0011.png", 0.033,
    "images/frames/murcielagos_0012.png", 0.033,
    "images/frames/murcielagos_0013.png", 0.033,
    "images/frames/murcielagos_0014.png", 0.033,
    "images/frames/murcielagos_0015.png", 0.033,
    "images/frames/murcielagos_0016.png", 0.033,
    "images/frames/murcielagos_0017.png", 0.033,
    "images/frames/murcielagos_0018.png", 0.033,
    "images/frames/murcielagos_0019.png", 0.033,
    "images/frames/murcielagos_0020.png", 0.033,
    "images/frames/murcielagos_0021.png", 0.033,
    "images/frames/murcielagos_0022.png", 0.033,
    "images/frames/murcielagos_0023.png", 0.033,
    "images/frames/murcielagos_0024.png", 0.033,
    "images/frames/murcielagos_0025.png", 0.033,
    "images/frames/murcielagos_0026.png", 0.033,
    "images/frames/murcielagos_0027.png", 0.033,
    "images/frames/murcielagos_0028.png", 0.033,
    "images/frames/murcielagos_0029.png", 0.033,
    "images/frames/murcielagos_0030.png", 0.033,
    "images/frames/murcielagos_0031.png", 0.033,
    "images/frames/murcielagos_0032.png", 0.033,
    "images/frames/murcielagos_0033.png", 0.033,
    "images/frames/murcielagos_0034.png", 0.033,
    "images/frames/murcielagos_0035.png", 0.033,
    "images/frames/murcielagos_0036.png", 0.033,
    "images/frames/murcielagos_0037.png", 0.033,
    "images/frames/murcielagos_0038.png", 0.033,
    "images/frames/murcielagos_0039.png", 0.033,
    "images/frames/murcielagos_0040.png", 0.033,
    "images/frames/murcielagos_0041.png", 0.033,
    "images/frames/murcielagos_0042.png", 0.033,
    "images/frames/murcielagos_0043.png", 0.033,
    "images/frames/murcielagos_0044.png", 0.033,
    "images/frames/murcielagos_0045.png", 0.033,
    "images/frames/murcielagos_0046.png", 0.033,
    "images/frames/murcielagos_0047.png", 0.033,
    "images/frames/murcielagos_0048.png", 0.033,
    "images/frames/murcielagos_0049.png", 0.033,
    "images/frames/murcielagos_0050.png", 0.033,
    "images/frames/murcielagos_0051.png", 0.033,
    "images/frames/murcielagos_0052.png", 0.033,
    "images/frames/murcielagos_0053.png", 0.033,
    repeat=False
)
