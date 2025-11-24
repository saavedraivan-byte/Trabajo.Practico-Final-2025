from gestor_turno import Peluqueria

def mostrar_menu():
    print("---------------------")
    print("SISTEMA DE TURNOS DE PELUQUERIA")
    print("1. Registrar nuevo cliente")
    print("2. Solicitar turno")
    print("3. Lista turnos existentes")
    print("4. Modificar turno")
    print("5. Cancelar turno")
    print("6. Guardar datos en CSV")
    print("7. Cargar turnos en CSV")
    print("8. Salir")
    print("---------------------")

def main():
    gestion = Peluqueria(
        "cliente.csv",
        "turno.csv",
        "profesional.csv",
        "slot_diciembre.csv",
        "servicio.csv"
    )
    

    while True:
        mostrar_menu()
        opciones = input("Escoger opcion: ")

        if opciones == "1":
            gestion.registrar_cliente()
        elif opciones == "2":
            gestion.solicitar_turno()
        elif opciones == "3":
            gestion.listar_turno()
        elif opciones == "4":
            gestion.modificar_turno()
        elif opciones == "5":
            gestion.cancelar_turno()
        elif opciones == "6":
            gestion.guardar_turno_csv()
        elif opciones == "7":
            gestion.cargar_turno_csv()
        elif opciones == "8":
            print("Saliendo del sistema")
            break
        
        else:
            print("Opcion incorrecta, Ingrese de nuevo")

if __name__ == "__main__":
    main()