
   

def guardar_cliente_csv(lista_cliente, nombre_archivo = "cliente.csv"):
        archivos = open(nombre_archivo, "wt") #abre en estricura
        archivos.write("nombre,apellido,DNI,edad,fecha_nacimiento,telefono\n")
        i = 0
        while i < len(lista_cliente):
            id_cliente = lista_cliente[i]
            linea = (
                id_cliente ["nombre"] + "," + 
                id_cliente ["apellido"] + "," +
                id_cliente ["DNI"] + "," +
                id_cliente ["edad"] + "," +
                id_cliente ["fecha_nacimiento"] + "," +
                id_cliente ["telefono"] + "\n"
            ) #se ingresa los valores con respectivos encabezados

            archivos.write(linea)
            i = i + 1

        archivos.close()
        print("Cliente guardado correctamente")

def carga_cliente_csv(nombre_archivo = "cliente.csv"):
     try:
        archivos = open(nombre_archivo, "rt")
        lineas = archivos.readlines()
        archivos.close()
     except FileNotFoundError:
           print("No se encontró el archivo del cliente. Se creará uno nuevo al guardar")
           return []
     clientes = []
     i = 1 # aca saltamos las keys
     while i < len(lineas):
          s = lineas[i].strip()
          if s == "":
               i = i + 1
               continue
          
          a = s.split(",")
          if len(a) < 5:
               print(f"Línea incompleta en CSV: {s}")
               i = i + 1
               continue

          
          cliente = {
               "nombre" : a[0],
               "apellido" : a[1],
               "DNI" : a[2],
               "edad" : a[3],
               "fecha_nacimiento" : a[4],
               "telefono" : a[5]
          }
          clientes.append(cliente) # guarda lo clientes en la lista de clientes
          i = i + 1
     return clientes
      
           

