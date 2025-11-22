

def crea_csv(nombre_archivo, columnas):
    file = open(nombre_archivo, "wt")
    csv_line = ",".join(columnas) + "\n"
    file.writelines([csv_line])
    file.close()

def agregar_valores_csv(nombre_archivo):
    file = open(nombre_archivo, "at")
    id_turno = input("Ingrese ID turno: ")
    while id_turno != "":
        DNI_cliente = input("Ingrese DNI: ")
        fecha = input("Ingrese fecha: ")
        hora = input("Ingrese hora: ")
        tipo_servicio = input("Ingrese servicio: ")
        vector = [id_turno,DNI_cliente,fecha,hora,tipo_servicio]
        fila = ",".join(vector) + "\n"
        file.writelines(fila)
        id_turno = input("Ingrese nombre: ")
    file.close()

crea_csv("turno.csv", ["id_turno", "DNI_cliente", "fecha", "hora", "tipo_servicio" ])
agregar_valores_csv("turno.csv")