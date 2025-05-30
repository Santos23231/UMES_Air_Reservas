class Cliente:
    def __init__(self, id, nombres, apellidos, nacionalidad, fecha_nacimiento, sexo, documento, email, celular, emergencia):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.documento = documento
        self.email = email
        self.celular = celular
        self.emergencia = emergencia

    def to_dict(self):
        return self.__dict__