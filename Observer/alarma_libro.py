from subject import Subject
from ilibro_mal_estado import ILibroMalEstado

# Clase AlarmaLibro que actúa como Observable
class AlarmaLibro:
    def __init__(self):
        self._observadores = []

    def add_observer(self, observador):
        self._observadores.append(observador)

    def remove_observer(self, observador):
        self._observadores.remove(observador)

    def notify_observers(self, mensaje):
        for observador in self._observadores:
            observador.update(mensaje)

    def dispara_alarma(self, libro):
        mensaje = f"Rompieron el libro, {libro.get_titulo()}"
        print(mensaje)
        self.notify_observers(mensaje)
