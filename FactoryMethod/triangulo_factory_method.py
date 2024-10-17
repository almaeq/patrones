from triangulo import Triangulo
from abc import ABC, abstractmethod

# Interfaz TrianguloFactoryMethod
class TrianguloFactoryMethod(ABC):
    @abstractmethod
    def create_triangulo(self, ladoA, ladoB, ladoC):
        pass
