from abc import ABC, abstractmethod

# Clase abstracta Triangulo
class Triangulo(ABC):
    def __init__(self, ladoA, ladoB, ladoC):
        self._ladoA = ladoA
        self._ladoB = ladoB
        self._ladoC = ladoC

    @abstractmethod
    def get_descripcion(self):
        pass

    @abstractmethod
    def get_superficie(self):
        pass

    @abstractmethod
    def dibujate(self):
        pass

    def get_ladoA(self):
        return self._ladoA

    def set_ladoA(self, ladoA):
        self._ladoA = ladoA