from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

def imprimir_informe(laptop):
    informe=laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")


laptop_carlos = Laptop("Lenovo", "i7", 32)
laptop_pedro = Laptop("Lenovo", "i7", 32, 600)

laptop_felipe = Laptop_Gaming("MSI", "I7", 4, "GTX 8GB")

#print(laptop_felipe.realizar_diagnostico_sistema())

laptop_point = Laptop_Business("Dell", "Intel i7", 16, "1TB", "10 horas")
#print(laptop_point.realizar_diagnostico_sistema())

print("PEDRO: ")
imprimir_informe(laptop_pedro)
print("FELIPE: ")
imprimir_informe(laptop_felipe)
