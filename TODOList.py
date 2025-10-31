# Importación de las librerias necesarias
import Utils as u
import Tarea as t

'''
    Atributos Globales
'''
listadoTareas = {}
ultimoID = -1

if __name__ == '__main__':

    listadoTareas = u.openJSON()
    MSG = ("Que operacion desea hacer: \n"
           "\t1 --> Listado de todas las tareas. \n"
           "\t2 --> Agregar una nueva tarea. \n"
           "\t3 --> Editar una tarea. \n"
           "\t4 --> Eliminar una tarea. \n"
           "\t5 --> Generar reporte (Número de tareas pendientes y completadas por prioridad). \n"
           "\t0 --> Salir. \n")
    opcion = -1
    while opcion != 0:
        opcion = int(input(MSG))
        if opcion == 1:
            u.listarTareas(listadoTareas)
        elif opcion == 2:
            u.addTarea(u.lastSetID())
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            u.generarReport()
        elif opcion == 0:
            print("Saliendo del programa TODO list.... ")
        else:
            print("Opcion no valida. ")
    else:
        u.guardarJSON()