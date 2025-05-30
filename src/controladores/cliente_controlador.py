from modelos.cliente import Cliente
from utilidades.gestor_archivos import guardar_cliente

def crear_cliente():
    print("=== Registrar cliente ===")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    nacionalidad = input("Nacionalidad: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    sexo = input("Sexo: ")
    documento = input("Pasaporte/DPI: ")
    email = input("Email: ")
    celular = input("Celular: ")
    emergencia = input("Contacto de emergencia: ")
    cliente = Cliente(
        id=documento,
        nombres=nombres,
        apellidos=apellidos,
        nacionalidad=nacionalidad,
        fecha_nacimiento=fecha_nacimiento,
        sexo=sexo,
        documento=documento,
        email=email,
        celular=celular,
        emergencia=emergencia
    )
    guardar_cliente(cliente.to_dict())
    print("Cliente registrado.")