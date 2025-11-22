

def crea_csv(nombre_archivo, columnas):
    file = open(nombre_archivo, "wt")
    csv_line = ",".join(columnas) + "\n"
    file.writelines([csv_line])
    file.close()

def agregar_valores_csv(nombre_archivo):
    file = open(nombre_archivo, "at")
    nombre = input("Ingrese nombre: ")
    while nombre != "":
        apellido = input("Ingrese apellido: ")
        dni = input("Ingrese DNI: ")
        edad = input("Ingrese edad: ")
        fecha_nac = input("Ingrese fecha nacimiento: ")
        telefono = input("Ingrese numero de telefono: ")
        vector = [nombre,apellido,dni,edad,fecha_nac,telefono]
        fila = ",".join(vector) + "\n"
        file.writelines(fila)
        nombre = input("Ingrese nombre: ")
    file.close()

crea_csv("cliente.csv", ["Nombre", "Apellido", "DNI", "Edad", "Fecha Nacimiento", "Telefono" ])
agregar_valores_csv("cliente.csv")

