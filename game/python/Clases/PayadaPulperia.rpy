
label Payada_Pulperia:
   
    python:

        from python.Clases.Payada import Payada
        from python.Clases.FrasePayada import FrasePayada
        from python.Clases.personajes import Personaje

        class PayadaPulperia(Payada):
            
            estimado = FrasePayada("Cómo le va mi estimado?", ambicion=0, humildad=1)
            cansado = FrasePayada("Lo veo cansado y sucio", ambicion=1, humildad=0)

            tirarse = FrasePayada("Venga a tirarse un rato", ambicion=0, humildad=1)
            banio = FrasePayada("Por que no se pega un baño", ambicion=1, humildad=0)

            yuyos = FrasePayada("A la sombra de los yuyos", ambicion=1, humildad=0)
            pucho1 = FrasePayada("Y después se me fuma un pucho", ambicion=0, humildad=1)

            tufo = FrasePayada("Que me está matando el tufo", ambicion=1, humildad=0)
            pucho2 = FrasePayada("Y después se me fuma un pucho", ambicion=0, humildad=1)

            # Enlazar nodos manualmente (sig_izq / sig_der)
            estimado.sig_izq = cansado

            cansado.sig_izq = tirarse
            cansado.sig_der = banio

            tirarse.sig_izq = yuyos
            tirarse.sig_der = pucho1

            banio.sig_izq = tufo
            banio.sig_der = pucho2

            # Estado local para la ronda de payada
            opciones_nodos = [estimado]
            
            def __init__(self, rondas=4, personaje:Personaje=None):
                super().__init__(rondas)
                self.personaje = personaje  # El personaje que habla

            def mostrar_dialogo(self, texto):
                """Muestra un diálogo en Ren'Py desde Python"""
                # renpy.exports.say(self.personaje, texto)
                self.personaje.hablar(texto,interact=False)

            def mostrar_menu(self, opciones):
                """Muestra un menú en Ren'Py y retorna la opción seleccionada"""
                menu_items = [(opcion.MostrarFrase(), opcion) for opcion in opciones if opcion is not None]
                
                if not menu_items:
                    return None
                
                # renpy.display_menu retorna el segundo elemento de la tupla
                return renpy.display_menu(menu_items)

            def payar(self):
                """Ejecuta la payada con diálogos mostrados en Ren'Py"""
                self._nivel_actual = 1
                self.frase_armada = []
                
                while self._nivel_actual <= self.cant_rondas:

                    # Seleccionar musica segun nivel y encolar para transición suave
                    if self._nivel_actual == 2:
                        renpy.music.queue("paya_1_B", relative_volume=0.5)
                    if self._nivel_actual == 3:
                        renpy.music.queue("paya_1_A", relative_volume=0.5)
                    if self._nivel_actual == 4:
                        renpy.music.queue("paya_1_B", relative_volume=0.5)

                    # Mostrar la payada acumulada
                    payada_texto = "\n".join([f.MostrarFrase() for f in self.frase_armada])
                    if payada_texto == "":
                        payada_texto = "..."
                    self.mostrar_dialogo(payada_texto)

                    # Construir menú con las opciones actuales
                    chosen = self.mostrar_menu(self.opciones_nodos)

                    if chosen is None:
                        # No hay más opciones: salimos del bucle
                        break

                    # Registrar elección
                    self.frase_armada.append(chosen)
                    renpy.store.ambicion = getattr(renpy.store, 'ambicion', 0) + chosen.ambicion
                    renpy.store.humildad = getattr(renpy.store, 'humildad', 0) + chosen.humildad

                    # Mostrar la payada actualizada
                    payada_texto = "\n".join([f.MostrarFrase() for f in self.frase_armada])
                    self.mostrar_dialogo(payada_texto)

                    # Reinicio la lista de texto para el siguiente nivel
                    if self._nivel_actual == self.cant_rondas - 1:
                        self.frase_armada = []

                    # Preparar las opciones del siguiente nivel
                    siguientes = []
                    if chosen.sig_izq:
                        siguientes.append(chosen.sig_izq)
                    if chosen.sig_der:
                        siguientes.append(chosen.sig_der)
                    self.opciones_nodos = siguientes

                    

                    self._nivel_actual += 1
                    
                    
                        