def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    if altura <= 0 or peso <= 0:
        print("Revisa tus datos, alguno de ellos es erróneo.")
    else:
        indice = peso / altura**2
        if indice < 20:
            print(str("PESO BAJO"))
        elif  20 <= indice < 25:
            print(str("NORMAL"))
        elif 25 <= indice < 30:
            print(str("SOBREPESO"))
        elif 30 <= indice < 40:
            print(str("OBESIDAD"))
        else:
            print(str("OBESIDAD MORBIDA"))

#no se como hacer que no me dé error cuando es division en 0
    
    




if __name__=='__main__':
    main()