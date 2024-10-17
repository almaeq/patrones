from tv_abstract_factory import TvAbstractFactory
from azul import Azul
from lcd import LCD

# Fábrica concreta FactoryLcdAzul que implementa TvAbstractFactory
class FactoryLcdAzul(TvAbstractFactory):
    def create_color(self):
        return Azul()

    def create_tv(self):
        return LCD()
