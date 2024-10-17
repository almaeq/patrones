from tv_abstract_factory import TvAbstractFactory
from amarillo import Amarillo
from plasma import Plasma

# Fábrica concreta FactoryPlasmaAmarillo que implementa TvAbstractFactory
class FactoryPlasmaAmarillo(TvAbstractFactory):
    def create_color(self):
        return Amarillo()

    def create_tv(self):
        return Plasma()
