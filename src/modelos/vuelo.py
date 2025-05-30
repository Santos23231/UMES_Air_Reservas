class Vuelo:
    def __init__(self, codigo, fecha, origen, destino, hora_salida, hora_llegada, capacidad, asientos_ocupados):
        self.codigo = codigo
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.capacidad = capacidad
        self.asientos_ocupados = asientos_ocupados

    def to_dict(self):
        return self.__dict__