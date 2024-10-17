from tv import TV

# Clase Plasma que hereda de TV
class Plasma(TV):
    def __init__(self, marca="", pulgadas=0, color="", precio=0.0, angulo_vision=0.0, tiempo_respuesta=0.0):
        super().__init__(marca, pulgadas, color, precio)
        self._angulo_vision = angulo_vision
        self._tiempo_respuesta = tiempo_respuesta
        self.set_descripcion("Plasma... próximamente será un LED")

    def get_angulo_vision(self):
        return self._angulo_vision

    def set_angulo_vision(self, angulo_vision):
        self._angulo_vision = angulo_vision

    def get_tiempo_respuesta(self):
        return self._tiempo_respuesta

    def set_tiempo_respuesta(self, tiempo_respuesta):
        self._tiempo_respuesta = tiempo_respuesta
