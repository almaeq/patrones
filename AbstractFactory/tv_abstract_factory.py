from abc import ABC, abstractmethod
from color import Color
from tv import TV

# Clase abstracta TvAbstractFactory
class TvAbstractFactory(ABC):
    @abstractmethod
    def create_color(self) -> Color:
        pass

    @abstractmethod
    def create_tv(self) -> TV:
        pass
