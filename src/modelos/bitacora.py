from datetime import datetime

class Bitacora:
    def __init__(self, usuario, accion, resultado):
        self.timestamp = datetime.now().isoformat()
        self.usuario = usuario
        self.accion = accion
        self.resultado = resultado

    def to_dict(self):
        return self.__dict__