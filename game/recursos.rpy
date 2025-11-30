define san = Character("Santos Vega", color = "#d6b707")
#define p_san = Character("Santos Vega", color = "#d6b707")   #PARA CLASE PERSONAJE
define viejo = Character("Don Ernesto", color= "#b81c07")

#define p_viejo = Character("Don Ernesto", color= "#b81c07")     #PARA CLASE PERSONAJE
define diablo = Character("Mandinga", color= "#b81c07")
define payador = Character("Payador del Pueblo", color = "#0abe79")  
define narrator = Character(None)
define basilisco = Character("Basilisco", color= "#ff7300")
define juan = Character("Juan Sin Ropa", color= "#b81c07")
define juan_oculto = Character("Gaucho", color= "#b81c07")
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
image santos_int_cueva = "images/sprites/Santos_en_Trono.png"
image santos_guitarra_rota ="/images/sprites/de ultimo momento/SV tocando la guitarra sorprendido-Photoroom.png"
image santos_recostado="/images/sprites/de ultimo momento/SV durmiendo con los ojos abiertos.png"
image santos_hablando_guitarra="/images/sprites/de ultimo momento/SantosHablandoConGuitarra.png"

image santos_arrogante_1 ="/images/sprites/de ultimo momento/Arrogante1.png"
image santos_arrogante_2 ="/images/sprites/de ultimo momento/Arrogante2.png"

image santos_asustado = "/images/sprites/de ultimo momento/SantosAsustado.png"

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
# image viejo_malo = "images/sprites/viejo_malo_s.png"
image viejo_hablando = "images/sprites/viejo de la pulperia de pie hablando.png"
image viejo_diabolico ="/images/sprites/de ultimo momento/viejoDiabolico.png"


image rival_payador = "images/sprites/Payador_2_en_interiorPulperia_2.png"
image payador_cantando = "images/sprites/Payador_guitarra_en_interiorPulperia_2.png"
image payador_enojado="images/sprites/de ultimo momento/payador cara de enojado-Photoroom.png"
image payador_sentado = "/images/sprites/de ultimo momento/payador con un baso.png"


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
image overlay_pesadilla = "images/fondos/ensuenio.png"

# sprites ombu
image juan_hablando = "images/sprites/JuanSinRopa_hablando.png"
image juan_guitarra = "images/sprites/JuanSinRopa_guitarra.png"
image santos_durmiendo_ombu = "images/sprites/Santos_dormido_ombu.png"
image serpiente_ombu = "images/sprites/serpiente_ombu.png"

image ombu = "images/fondos/ombu_conSombraSantosDurmiendo.png"
image ombu2 = "images/fondos/ombu.png"

# Un filtro negro semitransparente
image fondo_negro = Solid("#00000083")
image pantalla_negra = Solid ("#000000ff")
image pantalla_roja = Solid ("#b50000")
image pantalla_gris = Solid ("#b5b5b5ff")

define slowfade = Fade(2.0, 0.0, 2.0)

define fin_payada_intensa = "audio/finpayadaintensa.mp3"
define payada_intensa = "audio/payadaintensa.mp3"
define payada_feliz = "audio/payadaalegre.mp3"
define misterio = "audio/misterio.mp3"
define musica_intro = "audio/Nuevos/Santos Vega_Musica_Intro.mp3"
define musica_mandinga = "audio/Nuevos/Cueva_Mandinga.mp3"

# define paya_1_A = "audio/Nuevos/Primer_Paya/Paya_Frase_1.ogg"
# define paya_1_B = "audio/Nuevos/Primer_Paya/Paya_Frase_2.ogg"
# define paya_1_final = "audio/Nuevos/Primer_Paya/Paya_FinalCorte.ogg"
define paya_1_enganche = "audio/Nuevos/Primer_Paya/Paya_FinalConEnganche.mp3"
define paya_1_AyB = "audio/Nuevos/Primer_Paya/Paya_completa_loop.mp3"

define paya_1_A = "audio/Nuevos/PayadaCorta/Frase1.ogg"
define paya_1_B = "audio/Nuevos/PayadaCorta/Frase2.ogg"
define paya_1_final = "audio/Nuevos/PayadaCorta/FraseFinal.ogg"

define paya_2_intro = "audio/Nuevos/PayadaEpica/intro.ogg"
define paya_2_A = "audio/Nuevos/PayadaEpica/Frase1.ogg"
define paya_2_B = "audio/Nuevos/PayadaEpica/Frase2.ogg"
define paya_2_Final = "audio/Nuevos/PayadaEpica/final.ogg"
define paya_2_Completa = "audio/Nuevos/PayadaEpica/completa.ogg"


define alimanias_1 ="audio/SFX marcos/Alimanias1.ogg"
define alimanias_2 ="audio/SFX marcos/Alimanias2.ogg"
define sfx_asustado = "audio/SFX marcos/SantosAsustado.ogg"

define arpa_1 = "audio/SFX marcos/Arpa_1.ogg"
define arpa_2 = "audio/SFX marcos/Arpa_2.ogg"

define sfx_afligido = "/audio/SFX marcos/SFX_Gemido2.ogg"
define sfx_pasos_pasto = "/audio/SFX marcos/Pisadas_JuansSinRopa.ogg"
define sfx_risa_hombre = "/audio/SFX marcos/SFX-risa-santos.ogg"
define sfx_indignado ="/audio/SFX marcos/Sorpresa enojado.ogg"
define sfx_risa_diabolica="/audio/SFX marcos/Risa_3.ogg"
define sfx_grunido="/audio/SFX marcos/Santos_Enojado_Murmuro.ogg"
define sfx_guitarra_rota="/audio/SFX marcos/SFX_Guitarra_Rota.ogg"
define sfx_risa_jactante="/audio/SFX marcos/Risa_2.ogg"
define sfx_grito_derrota="/audio/SFX marcos/Grito_Derrota.ogg"
define sfx_grillos = "audio/Sonidos/grillo.mp3"

define sfx_pisadas_pasto ="/audio/SFX marcos/Pisadas_Pasto.ogg"

define sfx_murmuro_enojado = "/audio/SFX marcos/Murmuro_Enojado_1.ogg"
define sfx_murmuro_viejo = "/audio/SFX marcos/sfxMurmuro_viejo.ogg"
define sfx_sorbo = "/audio/SFX marcos/sfx_sorbo.ogg"

define sfx_risa_mandinga = "/audio/SFX marcos/Risa_Mandinga.ogg"

define brisa = "audio/Sonidos/brisa.mp3"
define puerta = "audio/Sonidos/puerta.mp3"
define sound_bat = "audio/Sonidos/murcielagos_flapping-sound.wav"
define sound_heart_loop= "audio/Sonidos/heartbeat-loop.wav"
define sound_heart = "audio/Sonidos/heartbeats-imperfections.wav"
define serpiente = "audio/Sonidos/serpiente.wav"
define risa_devil= "audio/Sonidos/flail-demon-laugh.wav"
define aplausos = "audio/Sonidos/aplausos__shagger.wav"
define sonido_caballo = "audio/sonidos_nuevos/relincho.wav"
define sonido_rocaCueva = "audio/sonidos_nuevos/rocaCueva2.wav"
define latidos_scare = "audio/sonidos_nuevos/latidos_scare3.wav"
define latidos_completo = "audio/sonidos_nuevos/latidos_scare.mp3"
define carcajadasFinSalamanca = "audio/sonidos_nuevos/carcajadasDiabolicasFinSalamanca.wav"
define suspiro_scare = "audio/sonidos_nuevos/suspiro_ghost-sigh3.wav"
define campo_noche = "audio/sonidos_nuevos/campoNoche.wav"
define campo_dia = "audio/sonidos_nuevos/amanecerCampo.wav"

transform saltito:
    zoom 1.05
    yoffset 0
    linear 0.08 yoffset 10
    linear 0.08 yoffset 0
    linear 0.08 yoffset 10
    linear 0.08 yoffset 0
    zoom 1.0

transform salto_tiembla:
    xoffset 0
    linear 0.08 xoffset 15
    linear 0.08 xoffset 0
    repeat 2

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

image sangre = Animation(
    "images/sangre/sangre0001.png", 0.033,
    "images/sangre/sangre0002.png", 0.033,
    "images/sangre/sangre0003.png", 0.033,
    "images/sangre/sangre0004.png", 0.033,
    "images/sangre/sangre0005.png", 0.033,
    "images/sangre/sangre0006.png", 0.033,
    "images/sangre/sangre0007.png", 0.033,
    "images/sangre/sangre0008.png", 0.033,
    "images/sangre/sangre0009.png", 0.033,
    "images/sangre/sangre0010.png", 0.033,
    "images/sangre/sangre0011.png", 0.033,
    "images/sangre/sangre0012.png", 0.033,
    "images/sangre/sangre0013.png", 0.033,
    "images/sangre/sangre0014.png", 0.033,
    "images/sangre/sangre0015.png", 0.033,
    "images/sangre/sangre0016.png", 0.033,
    "images/sangre/sangre0017.png", 0.033,
    "images/sangre/sangre0018.png", 0.033,
    "images/sangre/sangre0019.png", 0.033,
    "images/sangre/sangre0020.png", 0.033,
    "images/sangre/sangre0021.png", 0.033,
    "images/sangre/sangre0022.png", 0.033,
    "images/sangre/sangre0023.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    "images/sangre/sangre0024.png", 0.033,
    repeat=False
)