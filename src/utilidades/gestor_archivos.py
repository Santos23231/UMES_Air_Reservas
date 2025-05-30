import os
import json

# Rutas de archivos
RUTA_USUARIOS = os.path.join("datos", "usuarios.txt")
RUTA_CLIENTES = os.path.join("datos", "clientes.txt")
RUTA_VUELOS = os.path.join("datos", "vuelos.txt")
RUTA_RESERVAS = os.path.join("datos", "reservas.txt")
RUTA_BITACORA = os.path.join("datos", "bitacora.txt")

# Usuarios
def cargar_usuarios():
    usuarios = []
    with open('c:/UMES_Air_Reservas/datos/usuarios.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            try:
                usuario = json.loads(linea.strip())
                usuarios.append(usuario)
            except json.JSONDecodeError:
                print("Error al leer un usuario. Línea ignorada.")
    return usuarios

def guardar_usuario(usuario):
    with open(RUTA_USUARIOS, "a", encoding="utf-8") as f:
        f.write(json.dumps(usuario) + "\n")


def cargar_clientes():
    if not os.path.exists(RUTA_CLIENTES):
        return []
    with open(RUTA_CLIENTES, "r", encoding="utf-8") as f:
        return [json.loads(linea) for linea in f if linea.strip()]

def guardar_cliente(cliente):
    with open(RUTA_CLIENTES, "a", encoding="utf-8") as f:
        f.write(json.dumps(cliente) + "\n")

# Vuelos
def cargar_vuelos():
    if not os.path.exists(RUTA_VUELOS):
        return []
    with open(RUTA_VUELOS, "r", encoding="utf-8") as f:
        return [json.loads(linea) for linea in f if linea.strip()]

def guardar_vuelo(vuelo):
    with open(RUTA_VUELOS, "a", encoding="utf-8") as f:
        f.write(json.dumps(vuelo) + "\n")

# Reservas
def cargar_reservas():
    if not os.path.exists(RUTA_RESERVAS):
        return []
    with open(RUTA_RESERVAS, "r", encoding="utf-8") as f:
        return [json.loads(linea) for linea in f if linea.strip()]

def guardar_reserva(reserva):
    with open(RUTA_RESERVAS, "a", encoding="utf-8") as f:
        f.write(json.dumps(reserva) + "\n")

# Bitácora
def cargar_bitacora():
    if not os.path.exists(RUTA_BITACORA):
        return []
    with open(RUTA_BITACORA, "r", encoding="utf-8") as f:
        return [json.loads(linea) for linea in f if linea.strip()]

def guardar_bitacora(bitacora):
    with open(RUTA_BITACORA, "a", encoding="utf-8") as f:
        f.write(json.dumps(bitacora) + "\n")
