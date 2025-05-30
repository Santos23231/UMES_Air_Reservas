from modelos.usuario import Usuario
from modelos.cliente import Cliente
from utilidades.gestor_archivos import guardar_usuario

def crear_usuario():
    print("=== Crear usuario ===")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")
    rol = input("Rol (administrador/agente/pasajero): ")
    usuario = Usuario(
        id=correo,
        nombre=nombre,
        correo=correo,
        hash_contraseña=(contraseña),
        rol=rol
    )
    guardar_usuario(usuario.to_dict())
    print("Usuario creado.")
