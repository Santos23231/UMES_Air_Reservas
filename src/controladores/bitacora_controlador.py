from modelos.bitacora import Bitacora
from utilidades.gestor_archivos import guardar_bitacora

def registrar_accion(usuario, accion, resultado):
    bitacora = Bitacora(
        usuario=usuario,
        accion=accion,
        resultado=resultado
    )
    guardar_bitacora(bitacora.to_dict())