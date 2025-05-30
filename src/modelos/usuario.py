class Usuario:
    def __init__(self, id, nombre, correo, hash_contraseña, rol):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.hash_contraseña = hash_contraseña
        self.rol = rol

    def to_dict(self):
        return self.__dict__