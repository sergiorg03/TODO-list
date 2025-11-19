'''Fichero para la generación de reportes de las tareas. '''
# Importamos las librerias necesarias
import utils as u
import json
import Tarea as t


def generarReport(listadoTareas=None):
    """
        DEPRECATED
        Función que genera un reporte sobre las tareas pendientes y las realizadas en orden de prioridad.

        :param:
            listadoTareas --> Listado de tareas de las que haremos el reporte.

        :returns:
            Diccionario --> Devuelve un diccionario con clave tareas completadas y sin completar y valores las propias tareas.
    """
    if listadoTareas is None:
        listadoTareas = {}

    tareasSinCompletar = {}
    tareasCompletadas = {}

    for k, v in list(listadoTareas.items()):
        if v.completada:
            tareasCompletadas[k] = v.__str__()
        else:
            tareasSinCompletar[k] = v.__str__()

    return {"Tareas completadas": len(tareasCompletadas), "Tareas sin completar": len(tareasSinCompletar)}

def getTareasCompletadas(listadoTareas, completado:bool, item=1):
    '''

        Función recursiva que devuelve las tareas completadas de un listado de tareas.


        :param listadoTareas: Listado de tareas del que obtener las tareas completadas.
        :param completado: Booleano que indica si se buscan tareas completadas (True) o no completadas (False).
        :param item: Índice actual de la tarea a comprobar.


        :return Integer: Número de tareas completadas.
    '''
    cont = 0    
    try:
        
        cont = 1 if listadoTareas[str(item)].completada == completado else 0
        
    except KeyError:
        return cont
    else:
        return cont + getTareasCompletadas(listadoTareas,completado, item + 1)