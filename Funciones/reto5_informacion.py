import datetime

# Datos de entrada
datos = [
    "Antonio Moreno 2000",
    "Carmen Díaz 2001",
    "Fernando García 2003",
    "Teresa Rodríguez 2004",
    "José López 2005",
    "Miguel Ángel Ortiz 1999",
    "Lucia Gómez 2000",
    "Francisco Javier Sánchez 2001",
    "Beatriz Domínguez 2002",
    "Adrián López 2011",
    "Martina Pascual 2012",
    "Álvaro Torres 2013",
    "Berta Romero 2014"
]

# Funciones
def obtener_año_actual():
    return datetime.datetime.now().year

def agregar_nombre(info):
    nombre = " ".join(info.split()[:-1])  # Todos los elementos excepto el último
    nombre_paciente.append(nombre)

def agregar_edad(info):
    año_nacimiento = int(info.split()[-1])  # Último elemento
    edad_actual = año_actual - año_nacimiento
    edad.append(edad_actual)

# Variables
nombre_paciente = []
edad = []
año_actual = obtener_año_actual()  # Año actual

# Procesar los datos
for dato in datos:
    agregar_nombre(dato)
    agregar_edad(dato)

# Imprimir la lista de los nombres
print("Lista de nombres:", nombre_paciente)

# Imprimir la lista de las edades
print("Lista de edades:", edad)

# Imprimir cual paciente es mayor y menor
mayor = max(edad)
menor = min(edad)

indice_mayor = edad.index(mayor)
indice_menor = edad.index(menor)

print(f"{nombre_paciente[indice_mayor]} con la edad de {mayor} años es mayor a los demás pacientes.")
print(f"{nombre_paciente[indice_menor]} con la edad de {menor} años es menor a los demás pacientes.")
