from transformador import Transforma

def carga_archivo(nombre_archivo):
    archivo_cliente = open(nombre_archivo, "rt")
    clave_cliente = archivo_cliente.readline().strip()
    cliente = Transforma(clave_cliente)
    lista_cliente = []

    linea_cliente = archivo_cliente.readline()
    while linea_cliente != "":
        if linea_cliente == "\n":
            linea_cliente = archivo_cliente.readline()
            continue
        d = cliente.strtoDict(linea_cliente)
        if d is not None:
            lista_cliente.append(d)
        linea_cliente = archivo_cliente.readline()
    archivo_cliente.close()
    return lista_cliente


