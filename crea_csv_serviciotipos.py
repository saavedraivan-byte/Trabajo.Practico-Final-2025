

def crea_csv(nombre_archivo, columnas):
    file = open(nombre_archivo, "wt")
    csv_line = ",".join(columnas) + "\n"
    file.writelines([csv_line])
    file.close()

def agregar_valores_csv(nombre_archivo):
    file = open(nombre_archivo, "at")
    id_sevicio = input("Ingrese id_servicio: ")
    while id_sevicio != "":
        nombre = input("Ingrese nombre servicio: ")
        duracion = input("Ingrese duracion servicio: ")
        precio = input("Ingrese precio: ")
        profesional = input("Ingrese profesional: ")
        vector = [id_sevicio,nombre,duracion,precio,profesional]
        fila = ",".join(vector) + "\n"
        file.writelines(fila)
        id_sevicio = input("Ingrese id_servicio: ")
    file.close()

crea_csv("servicio.csv", ["Id_servicio", "Nombre_servicio", "Duracion_servicio", "Precio", "Profesional" ])
agregar_valores_csv("servicio.csv")
