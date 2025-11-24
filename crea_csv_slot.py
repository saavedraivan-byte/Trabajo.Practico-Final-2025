

def crea_csv(nombre_archivo, columnas):
    file = open(nombre_archivo, "wt")
    csv_line = ",".join(columnas) + "\n"
    file.writelines([csv_line])
    file.close()

def agregar_valores_csv(nombre_archivo):
    file = open(nombre_archivo, "at")
    fecha = input("Ingrese fecha de turno: ")
    while fecha != "":
        hora = input("Ingrese hora atencion: ")
        disponibilidad = input("Ingrese horario disponible: ")
        id_turno = input("Ingrese ID del turno: ")
        vector = [fecha,hora,disponibilidad,id_turno]
        fila = ",".join(vector) + "\n"
        file.writelines(fila)
        fecha = input("Ingrese fecha de turno: ")
    file.close()

crea_csv("slot_diciembre.csv", ["Fecha", "Hora", "Disponibilidad", "Id_turno" ])
agregar_valores_csv("slot_diciembre.csv")

