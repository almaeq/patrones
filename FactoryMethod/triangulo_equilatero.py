from triangulo import Triangulo

# Clase Equilatero que hereda de Triangulo
class Equilatero(Triangulo):
    def get_descripcion(self):
        return "Soy un Triangulo Equilatero"

    def get_superficie(self):
        # Aquí iría el algoritmo para calcular la superficie de un triángulo equilátero
        return 0

    def dibujate(self):
        # Aquí iría el algoritmo para dibujar un triángulo equilátero
        pass
