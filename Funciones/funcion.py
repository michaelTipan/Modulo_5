def bienvenida():
    print("Mis primeros pasos en funciones")

def datos(nombre, apellido, edad, mensaje="Hola"):
    if edad < 18:
        print(f"{mensaje} {nombre} {apellido} es menor de edad")
    else:
        print(f"{mensaje} {nombre} {apellido} es mayor de edad")

def encontrar_palabra(frase):
    if "feliz" in frase:
        print(f"El emmoji que te representa es: \U0001F600")
    elif "triste" in frase:
        print(f"El emmoji que te representa es: \U0001F614")

lista =[]
def agregar_frase(frase):
    lista.append(frase)
    print(f"La frase fue guardada correctamente: {lista}")