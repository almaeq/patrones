from ilibro_mal_estado import ILibroMalEstado

# Clase Stock que implementa ILibroMalEstado
class Stock(ILibroMalEstado):
    def update(self,mensaje):
        print("Stock: ", mensaje)
        print("Le doy de baja...")
