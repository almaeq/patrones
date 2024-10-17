from ilibro_mal_estado import ILibroMalEstado

# Clase Compras que implementa ILibroMalEstado
class Compras(ILibroMalEstado):
    def update(self, mensaje):
        print(f"Compras: {mensaje}")
        print("Solicito nueva cotización...")
