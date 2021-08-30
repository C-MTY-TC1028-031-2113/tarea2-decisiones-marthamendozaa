def main():
    # Escribe tu código abajo de esta línea
    grad = int(input("Introduce los grados: "))
    if grad > 0 and grad < 90:
        print("cuadrante 1")
    elif grad > 90 and grad < 180:
        print("cuadrante 2")
    elif grad > 180 and grad < 270:
        print("cuadrante 3")
    elif grad > 270 and grad < 360:
        print("cuadrante 4")
    elif grad == 0 or grad == 360 or grad == 90 or grad == 180 or grad == 270:
        print("eje")
    elif grad < 0 or grad > 360:
        print("excede")

if __name__ == '__main__':
    main()
