# Importación de las librerias necesarias
from sys import exec_prefix

import utils as u
import data_handler as d
import reports as r

'''
    Atributos Globales
'''
'''
    EJEMPLOS
    
    listadoTareas = {
        "1": Tarea(nombreTarea, descripcion, categoria={}, prioridad=3, completada=False),
        "2": Tarea2(nombreTarea, descripcion, categoria={}, prioridad=3, completada=False)
    }
listadoTareas = {
    "1" : t.Tarea("nombreTarea", "descripcion", {"1":"categoria"}, 3, False),
    "2" : t.Tarea("nombreTarea", "descripcion", {"1":"categoria", "2":"subcategoria"}, 3, False)
}'''
listadoTareas = {}
ultimoID = -1

if __name__ == '__main__':

    listadoTareas = d.openJSON() if d.openJSON() else {}
    MSG = ("\nQue operacion desea hacer: \n"
           "\t1 --> Listado de todas las tareas. \n"
           "\t2 --> Agregar una nueva tarea. \n"
           "\t3 --> Editar una tarea. \n"
           "\t4 --> Eliminar una tarea. \n"
           "\t5 --> Generar reporte (Número de tareas pendientes y completadas). \n"
           "\t6 --> Marcar una tarea como completada. \n"
           "\t7 --> Buscar una tarea por categoria o por prioridad. \n"
           "\t0 --> Salir. \n")
    opcion = -1
    while opcion != 0:
        try:
            opcion = int(input(MSG))
            match opcion:
                case 1: # Listamos las tareas
                    print(f"{u.listarTareas(listadoTareas=listadoTareas)}")
                case 2: # Añadimos una nueva tarea
                    ultimoID = u.lastSetID(listadoTareas=listadoTareas)
                    d.addTarea(ultimoIDUsado=ultimoID, listadoTareas=listadoTareas)
                    print("Tarea creada correctamente. ")
                case 3: # Editamos una tarea indicada
                    print("-"*40)
                    print(f"{u.listarTareas(listadoTareas=listadoTareas)}")
                    print("-"*40)
                    idTarea = input("Introduzca el ID de la tarea a editar: ").strip()

                    while not u.idInLista(listaTareas=listadoTareas, idTarea=idTarea):
                        idTarea = input("El id introducido no existe en la lista, introduce un ID correcto: \n")

                    d.editarTarea(listadoTareas= listadoTareas, idTareaEditar= idTarea)
                case 4: # Eliminamos una tarea
                    print(f"{u.listarTareas(listadoTareas=listadoTareas)}")
                    idTarea = input("Intrduzca el ID de la tarea que desea eliminar: \n")
                    while not u.isNumber(idTarea):
                        idTarea = input("Introduce un ID correcto: \n")
                    else:
                        d.eliminarTarea(listadoTareas=listadoTareas, IDTareaEliminar=idTarea)
                case 5: # Generación de reportes

                    totalTareas = 0
                    completadas = 0
                    print()
                    for k, v in r.generarReport(listadoTareas=listadoTareas).items():
                        '''print(f"\n{k}:\n")
                        for k2, v2 in v.items():
                            print(f"\tID: {k2} --> {v2}")'''
                        if k == "Tareas completadas":
                            completadas = v
                        print(f"El número de {k} es: {v}")
                        totalTareas += v

                    print(f"\nEl total de tareas es {totalTareas} y llevas un {((completadas/totalTareas)*100):.2f}% completado. \n")
                case 6: # Marcar tarea como completada
                    print(f"\n{u.listarTareas(listadoTareas=listadoTareas)}\n")
                    idTareaCompletar = input("Introduce el ID de la tarea a marcar como completada. \n")
                    while not u.idInLista(listaTareas=listadoTareas, idTarea=idTareaCompletar):
                        idTareaCompletar = input("El ID introducido no existe en la lista, introduce un ID correcto: \n")
                    if not listadoTareas[idTareaCompletar].completada:
                        listadoTareas[idTareaCompletar].completada = True
                        print("La tarea fue marcada como completada correctamente. \n")
                    else:
                        print(f"La tarea ya fue completada anteriormente. \n")
                case 7: # Buscar tarea por categoria o prioridad
                    op1 = -1
                    while op1 != 0:
                        try:
                            op1 = int(input(
                                "Introduzca 1 si desea buscar la tarea por categoria, 2 si desea buscar la tarea por prioridades o 0 si desea salir: \n"))

                            if op1 == 1: # Busqueda por categoria
                                cat = input("Introduzca la categoria que desea buscar: \n")
                                tareas = d.buscarTarea(listadoTareas=listadoTareas, categoria=cat)
                                for key, value in tareas.items():
                                    print(f"\tID: {key} --> {value.__str__()}")
                            elif op1 == 2: # Busqueda por prioridad
                                pri = -1
                                while not u.prioridadCorrecta(pri):
                                    try:
                                        pri = int(input("Introduzca la prioridad por la que desea buscar: "))
                                        tareas = d.buscarTarea(listadoTareas=listadoTareas, prioridad=pri)
                                        for key, value in tareas.items():
                                            print(f"\tID: {key} --> {value.__str__()}")
                                            print("\n")
                                    except ValueError:
                                        print("Opcion no valida. \n")
                            elif op1 == 0: # Saliendo de la busqueda de tareas
                                print("Saliendo de la busqueda de tareas... \n")
                            else:
                                print("Opcion no valida. \n")
                        except ValueError:
                            print("Opcion no valida. \n")

                case 0: # Salir del programa
                    print("Saliendo del programa TODO list.... ")
                case _: # Opcion introducida no valida
                    print("Opcion no valida. \n")

        except ValueError: # La opción introducida no es un número
            print("Opcion no valida. \n")
    else:
        d.guardarJSON(listadoTareas)