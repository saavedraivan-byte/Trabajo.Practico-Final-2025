from datetime import datetime
from cliente import Cliente
from turno import Turno 
from transformador import Transforma
from carga_archivo import carga_archivo
from clientes_agregar import guardar_cliente_csv, carga_cliente_csv




class Peluqueria(object):
    def __init__(self, cliente, turno, profesional, slot, servicio):
        self.cliente_transformador = Transforma("nombre,apellido,DNI,edad,fecha_nacimiento,telefono")
        self.id_turno_transformador = Transforma("id_turno,DNI_cliente,fecha,hora,tipo_servicio")
        #self.id_turno = []
        #self.cliente = []
        self.cliente = carga_cliente_csv(cliente)
        self.id_turno = carga_archivo(turno)
        self.profesional = carga_archivo(profesional)
        self.slot = carga_archivo(slot)
        self.servicio = carga_archivo(servicio)
        #self.profesional = []
        #self.servicio = []
        #self.slot = []



    def registrar_cliente(self):
        valors = self.cliente_transformador.in_values()
        #nuevo = Cliente(**valors)
        self.cliente.append(valors)
        print("Se a registrado al cliente ")

        guardar_cliente_csv(self.cliente)

    def solicitar_turno(self):
        i = 0
        print(" Servicios disponibles: ")
        while i < len(self.servicio):
            servi = self.servicio[i]
            print(f"{servi['Id_servicio']}-{servi['Nombre_servicio']}")
            i = i + 1

        s = input("Elegir Id servicio: ").strip()
        j = 0
        servicio_escogido = None 
        while j < len(self.servicio):
            if self.servicio[j]["Id_servicio"] == s:
                servicio_escogido = self.servicio[j]["Nombre_servicio"]
                break
            j = j + 1
        if servicio_escogido is None:
            print("Servicio no encontrado")
            return 
        
        dni = input("Ingresar DNI: ").strip()

        n = 0
        cliente_registrado = False
        while n < len(self.cliente):
            if self.cliente[n]["DNI"] == dni:
                cliente_registrado = True
                break
            n = n + 1
        
        if not cliente_registrado:
            print("El DNI no pertenece a ningun cliente registrado")
            print("Registre al cliente antes de poder solicitar el turno")
            return
        print("Turnos disponibles: ")
        m = 0
        disponibilidad = False
        while m < len(self.slot):
            slot = self.slot[m]
            if slot["disponibilidad"] == "True":
                print(f"- {slot['fecha']} a las {slot['hora']}")
                disponibilidad = True
            m = m + 1
        
        if not disponibilidad:
            print("No hay turnos disponibles")
            return
        
        fecha = input("Ingresar fecha: ").strip()
        hora = input("Ingresar hora: ").strip()

        try:
            fecha_turno = datetime.strptime(fecha + " " + hora, "%d-%m-%Y %H:%M")
        except ValueError:
            print("Formato de fecha, hora inválida")
            return
        

        validar_turno = False
        k = 0
        while k < len(self.slot):
            slot_act = self.slot[k]
            slot_date = datetime.strptime(slot_act["fecha"] + " " + slot_act["hora"], "%d-%m-%Y %H:%M")

            if slot_date == fecha_turno and slot_act["disponibilidad"] == "True":
                slot_act["disponibilidad"] = "False"
                validar_turno = True 
                break
            k = k + 1

        if not validar_turno:
            print("Este horario ya está ocupado, escoge otro")
            return

        turno_nuevo = len(self.id_turno) + 1
        turno = {
            "id_turno" : str(turno_nuevo),
            "DNI_cliente" : dni,
            "fecha" : fecha_turno.strftime("%d-%m-%Y"),
            "hora" : fecha_turno.strftime("%H:%M"),
            "tipo_servicio" : servicio_escogido if servicio_escogido else ""
        }

        self.id_turno.append(turno)
        print("Turno registrado")

        self.guardar_turno_csv()


    def listar_turno(self):
        if len(self.id_turno) == 0:
            print("No hay turnos disponibles")
            return
        i = 0
        print("Lista turnos")
        while i < len(self.id_turno):
            l = self.id_turno[i]
            print(f"ID:{l['id_turno']} / DNI:{l['DNI_cliente']} / Fecha:{l['fecha']} / Hora: {l['hora']} / Sevicio: {l['tipo_servicio']}")
            i = i + 1

    def modificar_turno(self):
        print("Turnos existentes: ")
        self.listar_turno()
        
        turno_modif = input("Ingrese el ID del turno a modificar: ").strip()
        i = 0
        turno_encontrado = None
        while i < len(self.id_turno):
            if self.id_turno[i]["id_turno"] == turno_modif:
                turno_encontrado = self.id_turno[i]
                break
            i = i + 1
        
        if turno_encontrado is None:
            print("No se encontró el turno")
            return
        
        n_fecha = input(F"Nueva fecha (actual: {turno_encontrado['fecha']}): ").strip()
        if n_fecha:
            turno_encontrado["fecha"] = n_fecha
        n_hora = input(f"Nueva hora (actual: {turno_encontrado['hora']}): ").strip()
        if n_hora:
            turno_encontrado["hora"] = n_hora
            

        print(" Servicios disponibles")
        k = 0
        while k < len(self.servicio):
            print(self.servicio[k]["Id_servicio"], "-", self.servicio[k]["Nombre_servicio"])
            k = k + 1


        n_servicio = input(f"Nuevo servicio (actual: {turno_encontrado['tipo_servicio']}): ").strip()    
        if n_servicio:
            turno_encontrado["tipo_servicio"] = n_servicio
        
        print("Turno modificado exitosamente")

        self.guardar_turno_csv         

    def cancelar_turno(self):
        print("Turnos existentes: ")
        self.listar_turno()

        id_acancelar = input("Ingrese el ID del turno a cancelar: ").strip()
        i = 0
        id_encontrado = False

        while i < len(self.id_turno):
            if self.id_turno[i]["id_turno"] == id_acancelar:
                id_encontrado = True
                break
            i = i + 1

        if not id_encontrado:
            print("Turno no encontrado")
            return
        
        n_lista = []
        j = 0
        while j < len(self.id_turno):
            if j != i:
                n_lista.append(self.id_turno[j])
            j = j + 1

        self.id_turno = n_lista
        print("Turno cancelado exitosamente")
        self.guardar_turno_csv

    def guardar_turno_csv(self, nombre_archivo = "turno.csv"):
        archivos = open(nombre_archivo, "wt")
        archivos.write("id_turno,DNI_cliente,fecha,hora,tipo_servicio\n")
        i = 0
        while i < len(self.id_turno):
            turno = self.id_turno[i]
            linea = (
                turno["id_turno"] + "," + 
                turno["DNI_cliente"] + "," +
                turno["fecha"] + "," +
                turno["hora"] + "," +
                turno["tipo_servicio"] + "\n"
            )

            archivos.write(linea)
            i = i + 1

        archivos.close()
        print("Turnos guardados correctamente")

    def cargar_turno_csv(self):
        self.id_turno = carga_archivo("turno.csv")
        print("Turnos cargados exitosamente")
        

gt = Peluqueria("cliente.csv", "turno.csv", "profesional.csv", "slot_diciembre.csv", "servicio.csv")

