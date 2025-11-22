from cliente import Cliente
from turno import Turno 
from transformador import Transforma
from carga_archivo import carga_archivo



class Peluqueria(object):
    def __init__(self):
        self.cliente_transformador = Transforma("nombre,apellido,DNI,edad,fecha_naci,telefono")
        self.id_turno_transformador = Transforma("id_turno,DNI_cliente,fecha,hora,tipo_servicio")
        self.id_turno = []
        self.cliente = []
        #self.profesional = []
        #self.servicio = []
        #self.slot = []



    def registrar_cliente(self):
        valors = self.cliente_transformador.in_values()
        nuevo = Cliente(**valors)
        self.cliente.append(nuevo)
        print("Se a registrado al cliente ")

    def solicitar_turno(self):
        valors = self.id_turno_transformador.in_values()
        nuevo = Turno(**valors)
        self.id_turno.append(nuevo)
        print("Se ah registrado el turno: ")

    def listar_turno(self):
        va

    def modificar_turno(self):
        pass

    def cancelar_turno(self):
        pass

    def guardar_turno_csv(self):
        pass

    def cargar_turno_csv(self):
        pass


