from abc import ABC, abstractmethod
from ilibro_mal_estado import ILibroMalEstado

# Interfaz Subject
class Subject(ABC):
    @abstractmethod
    def attach(self, observador: ILibroMalEstado):
        pass

    @abstractmethod
    def detach(self, observador: ILibroMalEstado):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
