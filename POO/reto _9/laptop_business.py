from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria
    
    def __str__(self):
        return f"Marca: {self.marca} \nProcesador: {self.procesador} \nMemoria: {self.memoria} \nAlmacenamiento: {self.almacenamiento} \nBateria: {self.duracion_bateria} \nPrecio: {self.costo}\n\n"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Resultado conectividad"] = resultado_conectividad
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        conectividad = {}
        conectividad["Disponibilidad de Wi-Fi"] = random.choice([True, False])
        conectividad["Acceso a servidores empresariales"] = random.choice([True, False])
        conectividad["Latencia de la red"] = random.choice([True, False])
        return conectividad


