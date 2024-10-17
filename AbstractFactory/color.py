from abc import ABC, abstractmethod

# Clase abstracta Color
class Color(ABC):
    def __init__(self):
        self._descripcion = ""

    @abstractmethod
    def colorea(self, tv):
        pass

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
