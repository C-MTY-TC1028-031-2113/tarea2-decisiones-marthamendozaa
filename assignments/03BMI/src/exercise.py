def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    indice = peso / altura**2
    if altura <= 0 or peso <= 0:
        print("Revisa tus datos, alguno de ellos es erróneo.")
    elif indice < 20:
        print(str("PESO BAJO"))
    elif  20 <= indice < 25:
        print(str("NORMAL"))
    elif 25 <= indice < 30:
        print(str("SOBREPESO"))
    elif 30 <= indice < 40:
        print(str("OBESIDAD"))
    elif indice >= 40:
        print(str("OBESIDAD MORBIDA"))
    
    
    




if __name__=='__main__':
    main()