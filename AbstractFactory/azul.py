from color import Color

# Clase Azul que hereda de Color
class Azul(Color):
    def __init__(self):
        super().__init__()
        self._es_primario = True

    def colorea(self, tv):
        print(f"Pintando de azul el {tv.get_descripcion()}")

    def is_es_primario(self):
        return self._es_primario

    def set_es_primario(self, es_primario):
        self._es_primario = es_primario
