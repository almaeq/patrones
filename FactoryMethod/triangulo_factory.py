from triangulo_factory_base import TrianguloFactoryBase
from triangulo_equilatero import Equilatero
from triangulo_escaleno import Escaleno
from triangulo_isosceles import Isosceles
from triangulo import Triangulo

# Clase concreta TrianguloFactory que implementa TrianguloFactoryBase
class TrianguloFactory(TrianguloFactoryBase):
    def create_triangulo(self, ladoA, ladoB, ladoC) -> Triangulo:
        if ladoA == ladoB and ladoA == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoB, ladoC)
