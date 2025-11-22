class Profesional(object):
    def __init__(self, nombre, apellido, horario):
        self.nombre = nombre
        self.apellido = apellido
        self.horario = horario
        self.servicios = []
        self.slot = []
        self.estado= False
        
    