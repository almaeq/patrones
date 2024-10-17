# Clase Libro
class Libro:
    def __init__(self, titulo, estado):
        self._titulo = titulo
        self._estado = estado

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado
