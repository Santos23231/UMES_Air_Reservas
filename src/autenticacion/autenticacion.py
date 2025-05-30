from utilidades.gestor_archivos import cargar_usuarios

def login():
    correo = input("Correo: ").strip()
    contrasena = input("Contraseña: ").strip()
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            return usuario
    print("Credenciales incorrectas.")
    return None