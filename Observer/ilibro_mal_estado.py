from abc import ABC, abstractmethod

# Interfaz ILibroMalEstado
class ILibroMalEstado(ABC):
    @abstractmethod
    def update(self):
        pass
