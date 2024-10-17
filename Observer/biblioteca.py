from alarma_libro import AlarmaLibro
from compras import Compras
from administracion import Administracion
from stock import Stock

# Clase Biblioteca
class Biblioteca:
    def devuelve_libro(self, libro):
        if libro.get_estado() == "MALO":
            alarma = AlarmaLibro()
            alarma.add_observer(Compras())
            alarma.add_observer(Administracion())
            alarma.add_observer(Stock())
            alarma.dispara_alarma(libro)
