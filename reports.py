'''Fichero para la generación de reportes de las tareas. '''
# Importamos las librerias necesarias
import utils as u
import json
import Tarea as t
import sklearn as skl


def generarReport(listadoTareas=None):  # TODO: Terminar método
    """
        Función que genera un reporte sobre las tareas pendientes y las realizadas en orden de prioridad.

        :param
            listadoTareas --> Listado de tareas de las que haremos el reporte.

        :returns
            dict --> Devuelve un diccionario con clave tareas completadas y sin completar y valores las propias tareas.
    """
    if listadoTareas is None:
        listadoTareas = {}

    tareasSinCompletar = {}
    tareasCompletadas = {}

    for k, v in list(listadoTareas.items()):
        if v.completada:
            tareasCompletadas[k] = v.toString()
        else:
            tareasSinCompletar[k] = v.toString()
        if v.subTareas:
            subtarea = generarReport(v.subTareas)
            tareasCompletadas.update(subtarea['Tareas completadas'])
            tareasSinCompletar.update(subtarea['Tareas sin completar'])

    return {"Tareas completadas": tareasCompletadas, "Tareas sin completar": tareasSinCompletar}