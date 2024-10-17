from ilibro_mal_estado import ILibroMalEstado

# Clase Administración que implementa ILibroMalEstado
class Administracion(ILibroMalEstado):
    def update(self,mensaje):
        print(f"Administración: {mensaje}")
        print("Envio una queja formal...")
