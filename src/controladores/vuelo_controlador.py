from modelos.vuelo import Vuelo
from utilidades.gestor_archivos import guardar_vuelo

def crear_vuelo():
    print("=== Crear vuelo ===")
    codigo = input("Código de vuelo: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    origen = input("Origen: ")
    destino = input("Destino: ")
    hora_salida = input("Hora de salida (HH:MM): ")
    hora_llegada = input("Hora de llegada (HH:MM): ")
    capacidad = int(input("Capacidad (máx 18): "))
    vuelo = Vuelo(
        codigo=codigo,
        fecha=fecha,
        origen=origen,
        destino=destino,
        hora_salida=hora_salida,
        hora_llegada=hora_llegada,
        capacidad=capacidad,
        asientos_ocupados=[]
    )
    guardar_vuelo(vuelo.to_dict())
    print("Vuelo creado.")