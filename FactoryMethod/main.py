from triangulo_factory import TrianguloFactory


def main():
    factory = TrianguloFactory()
    triangulo = factory.create_triangulo(20, 30, 10)
    print(triangulo.get_descripcion())

if __name__ == "__main__":
    main()
