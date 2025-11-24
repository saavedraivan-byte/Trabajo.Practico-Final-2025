

def crea_csv(nombre_archivo, columnas):
    file = open(nombre_archivo, "wt")
    csv_line = ",".join(columnas) + "\n"
    file.writelines([csv_line])
    file.close()

def agregar_valores_csv(nombre_archivo):
    file = open(nombre_archivo, "at")
    id_profesional = input("Ingrese ID Profesional: ")
    while id_profesional != "":
        nombre = input("Ingrese nombre Profesional: ")
        apellido = input("Ingrese apellido: ")
        servicio = input("Ingrese servicio: ")
        vector = [id_profesional,nombre,apellido,servicio]
        fila = ",".join(vector) + "\n"
        file.writelines(fila)
        id_profesional = input("Ingrese ID Profesional: ")
    file.close()

crea_csv("Profesional.csv", ["ID Profesional","Nombre", "Apellido", "Servicio" ])
agregar_valores_csv("Profesional.csv")
