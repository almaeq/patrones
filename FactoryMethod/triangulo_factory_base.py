from abc import ABC, abstractmethod
from triangulo import Triangulo

# Clase abstracta TrianguloFactoryMethod
class TrianguloFactoryBase(ABC):
    @abstractmethod
    def create_triangulo(self, ladoA, ladoB, ladoC) -> Triangulo:
        pass
