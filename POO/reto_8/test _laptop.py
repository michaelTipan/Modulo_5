from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop_carlos = Laptop("Lenovo", "i7", 32)
laptop_pedro = Laptop("Lenovo", "i7", 32, 600)

laptop_felipe = Laptop_Gaming("MSI", "I7", 4, "GTX 8GB")

#print(laptop_felipe.realizar_diagnostico_sistema())

laptop_point = Laptop_Business("Dell", "Intel i7", 16, "1TB", "10 horas")
print(laptop_point.realizar_diagnostico_sistema())