# Importación de las librerias necesarias
import utils as u
import data_handler as d
import reports as r
import sklearn as skl

'''
    Atributos Globales
'''
'''
    EJEMPLOS
    
    listadoTareas = {
        "1": Tarea(nombreTarea, descripcion, categoria, prioridad=3, completada=False, subTareas={}),
        "2": Tarea2(nombreTarea, descripcion, categoria, prioridad=3, completada=False, subTareas=
                                                                        {                            
                                                                        Tarea(nombreTarea, descripcion, categoria, prioridad=3, completada=False, subTareas={})
                                                                        })
    }
listadoTareas = {
    "1" : t.Tarea("nombreTarea", "descripcion", "categoria", 3, False, subTareas=None),
    "2" : t.Tarea("nombreTarea", "descripcion", "categoria", 3, False, subTareas={
            "2.1": t.Tarea("nombre", "descripcion", 3, False, True, None)
    })
}'''
listadoTareas = {}
ultimoID = -1

if __name__ == '__main__':

    listadoTareas = d.openJSON()
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
            print(f"{u.listarTareas(listadoTareas=listadoTareas)}")
        elif opcion == 2:
            d.addTarea(u.lastSetID(ultimoID), listadoTareas= listadoTareas)
        elif opcion == 3:
            pass
        elif opcion == 4:
            print(f"{u.listarTareas(listadoTareas=listadoTareas)}")
            idTarea = input("Intrduzca el ID de la tarea que desea eliminar: \n")
            while not u.isNumber(idTarea):
                idTarea = input("Introduce un ID correcto: \n")
            else:
                d.eliminarTarea(listadoTareas=listadoTareas, IDTareaEliminar=int(idTarea))
        elif opcion == 5:

            for k, v in r.generarReport(listadoTareas=listadoTareas).items():
                print(f"\n{k}:\n")
                for k2, v2 in v.items():
                    print(f"\tID: {k2} --> {v2}")
        elif opcion == 0:
            print("Saliendo del programa TODO list.... ")
        else:
            print("Opcion no valida. ")
    else:
        d.guardarJSON(listadoTareas)