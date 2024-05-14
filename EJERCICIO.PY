def agregar_tarea(tareas, descripcion):
    tarea = {"descripcion": descripcion, "completada": False}
    # Insertar la tarea al principio de la lista
    tareas.insert(0, tarea)
    print("Tarea agregada correctamente.")

def borrar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada correctamente.")
    else:
        print("Índice de tarea no válido.")

def marcar_completada(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Índice de tarea no válido.")

def ver_tareas(tareas):
    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i + 1}. {tarea['descripcion']} - {estado}")

def main():
    tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Ver tareas pendientes")
        print("4. Borrar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(tareas, descripcion)
        elif opcion == "2":
            ver_tareas(tareas)
            indice = int(input("Ingrese el número de la tarea completada: ")) - 1
            marcar_completada(tareas, indice)
        elif opcion == "3":
            ver_tareas(tareas)
        elif opcion == "4":
            ver_tareas(tareas)
            indice = int(input("Ingrese el número de la tarea a borrar: ")) - 1
            borrar_tarea(tareas, indice)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
