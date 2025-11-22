class Turno(object):
    def __init__(self, id_turno, DNI_cliente, fecha, hora, tipo_servicio):
        self.id_turno = id_turno
        self.DNI_cliente = DNI_cliente
        self.fecha = fecha
        self.hora = hora
        self.tipo_servicio = tipo_servicio

    