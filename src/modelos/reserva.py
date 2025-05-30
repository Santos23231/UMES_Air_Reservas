class Reserva:
    def __init__(self, pnr, id_cliente, id_vuelo, asiento, tarifa, estado):
        self.pnr = pnr
        self.id_cliente = id_cliente
        self.id_vuelo = id_vuelo
        self.asiento = asiento
        self.tarifa = tarifa
        self.estado = estado

    def to_dict(self):
        return self.__dict__