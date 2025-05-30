from modelos.reserva import Reserva
from utilidades.gestor_archivos import guardar_reserva

def crear_reserva():
    print("=== Crear reserva ===")
    pnr = input("Número de reserva (PNR): ")
    id_cliente = input("ID cliente: ")
    id_vuelo = input("ID vuelo: ")
    asiento = input("Asiento: ")
    tarifa = float(input("Tarifa: Q"))
    estado = input("Estado (pagada/pendiente/cancelada): ")
    reserva = Reserva(
        pnr=pnr,
        id_cliente=id_cliente,
        id_vuelo=id_vuelo,
        asiento=asiento,
        tarifa=tarifa,
        estado=estado
    )
    guardar_reserva(reserva.to_dict())
    print("Reserva creada.")