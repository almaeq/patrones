from abc import ABC, abstractmethod
import copy

# Clase abstracta TV
class TV(ABC):
    def __init__(self, marca="", pulgadas=0, color="", precio=0.0):
        self._marca = marca
        self._pulgadas = pulgadas
        self._color = color
        self._descripcion = ""
        self._precio = precio

    def clone(self):
        return copy.deepcopy(self)

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_pulgadas(self):
        return self._pulgadas

    def set_pulgadas(self, pulgadas):
        self._pulgadas = pulgadas

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
