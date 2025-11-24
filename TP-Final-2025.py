class Peluqueria(object):
    def __init__(self, id_turno, cliente, profesional, servicio, slot ):
        self.id_turno = id_turno
        self.cliente = cliente
        self.profesional = profesional
        self.servicio = servicio
        self.slot = slot
        


class Cliente(object):
    def __init__(self, nombre, apellido, id_cliente, edad, fecha_naci, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente
        self.edad = edad 
        self.fecha_naci = fecha_naci
        self.email = email
        self.telefono = telefono


class Servicio(object):
    def __init__(self, id_servicio, nombre, duracion, precio):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.duracion = duracion
        self.precio = precio

    

class Turno(object):
    def __init__(self, id_turno, id_cliente: Cliente, fecha, hora, tipo_servicio: Servicio):
        self.id_turno = id_turno
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.hora = hora
        self.tipo_servicio = tipo_servicio


class Slot(object):
    def __init__(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora
        self.ocupado = False
        self.id_turno = None



class Profesional(object):
    def __init__(self, nombre, id_profesional):
        self.nombre = nombre
        self.id_profesional = id_profesional
        self.slot = []
        self.servicio = []
    

class Transforma(object):
    def __init__(self, keys):
        self.keys = keys.split(",") #separo las llaves

    def strtoDict(self, values):
        file = values.split(",")
        if len(file) != len(self.keys):
            return None 
        d = {}
        i = 0
        while i < len(self.keys):
            d[self.keys[i]] = file[i] #igualo las filas en ambos
            i = i + 1
        return d 
