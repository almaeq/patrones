from tv import TV

# Clase LCD que hereda de TV
class LCD(TV):
    def __init__(self, marca="", pulgadas=0, color="", precio=0.0, costo_fabricacion=0.0):
        super().__init__(marca, pulgadas, color, precio)
        self._costo_fabricacion = costo_fabricacion
        self.set_descripcion("LCD")

    def get_costo_fabricacion(self):
        return self._costo_fabricacion

    def set_costo_fabricacion(self, costo_fabricacion):
        self._costo_fabricacion = costo_fabricacion
