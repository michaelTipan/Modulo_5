import funcion

cantidad_frase = int(input("Cuantas frases deasea ingresar: "))
for i in range(cantidad_frase):
    frase = input("Ingrese la frase: ")
    funcion.encontrar_palabra(frase)
    funcion.agregar_frase(frase)