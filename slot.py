class Slot_disponibilidad(object):
    def __init__(self, fecha, hora ):
        self.fecha = fecha
        self.hora = hora
        self.disponibilidad = False
        self.id_turno = None