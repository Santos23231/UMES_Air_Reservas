from controladores.usuario_controlador import crear_usuario
from controladores.vuelo_controlador import crear_vuelo
from controladores.cliente_controlador import crear_cliente
from controladores.reserva_controlador import crear_reserva

def menu_usuarios():
    while True:
        print("\n--- Gestión de usuarios ---")
        print("1. Crear usuario")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_vuelos():
    while True:
        print("\n--- Gestión de vuelos ---")
        print("1. Crear vuelo")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_vuelo()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_clientes():
    while True:
        print("\n--- Gestión de clientes ---")
        print("1. Crear cliente")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_reservas():
    while True:
        print("\n--- Gestión de reservas ---")
        print("1. Crear reserva")
        print("2. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_reserva()
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_admin():
    while True:
        print("\nMenú principal - Rol: administrador")
        print("1. Gestión de usuarios")
        print("2. Gestión de vuelos")
        print("3. Gestión de clientes")
        print("4. Reservas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_vuelos()
        elif opcion == "3":
            menu_clientes()
        elif opcion == "4":
            menu_reservas()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_usuario(usuario):
    while True:
        print("\nMenú principal - Rol: usuario")
        print("1. Gestión de vuelos")
        print("2. Gestión de clientes")
        print("3. Reservas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_vuelos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_reservas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_principal(usuario):
    while True:
        print("1. emitir pase de abordaje")
        print("2. mostrar reportes")
        print("3. Reportes operativos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            emitir_pase_abordaje(usuario)
        elif opcion == "2":
            if usuario["rol"] == "administrador":
                mostrar_reportes()
            else:
                print("Acceso solo para administradores.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def emitir_pase_abordaje(usuario):
    print("\n--- Emisión de pase de abordaje ---")
    reserva = {
        "nombre": usuario.get("Fabiola", "Hernandes "),
        "vuelo": "AV123",
        "asiento": "2C",
        "origen": "GUATEMALA",
        "destino": "Flores peten",
        "fecha": "2025-06-01",
        "hora": "10:00"
    }
    nombre_archivo = f"pase_abordaje_{reserva['nombre'].replace(' ', '_')}_{reserva['vuelo']}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("=== Pase de Abordaje ===\n")
        f.write(f"Pasajero: {reserva['nombre']}\n")
        f.write(f"Vuelo: {reserva['vuelo']}\n")
        f.write(f"Asiento: {reserva['asiento']}\n")
        f.write(f"Origen: {reserva['origen']}\n")
        f.write(f"Destino: {reserva['destino']}\n")
        f.write(f"Fecha: {reserva['fecha']}\n")
        f.write(f"Hora: {reserva['hora']}\n")
        f.write("========================\n")
    print(f"Pase de abordaje generado: {nombre_archivo}\n")

def mostrar_reportes():
    print("\n--- Reportes operativos ---")
    vuelos = [
        {"codigo": "AV123", "origen": "Guatemala", "destino": "Flores peten", "asientos_totales": 6, "asientos_ocupados": 4},
        {"codigo": "AV456", "origen": "Flores peten", "destino": "Guatemala ", "asientos_totales": 6, "asientos_ocupados": 2}
    ]

    print("Reporte de ocupación de vuelos:")
    for vuelo in vuelos:
        print(f"Vuelo: {vuelo['codigo']} | Origen: {vuelo['origen']} | Destino: {vuelo['destino']}")
        print(f"Asientos ocupados: {vuelo['asientos_ocupados']} / {vuelo['asientos_totales']}")
        print("-" * 40)

def mostrar_menu_admin_completo(usuario):
    while True:
        print("\n--- Menú administrador completo ---")
        print("1. Emitir pase de abordaje")
        print("2. Mostrar reportes")
        print("3. Gestión de usuarios")
        print("4. Gestión de vuelos")
        print("5. Gestión de clientes")
        print("6. Reservas")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            emitir_pase_abordaje(usuario)
        elif opcion == "2":
            mostrar_reportes()
        elif opcion == "3":
            menu_usuarios()
        elif opcion == "4":
            menu_vuelos()
        elif opcion == "5":
            menu_clientes()
        elif opcion == "6":
            menu_reservas()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
