'''Fichero para la generación de reportes de las tareas. '''
# Importamos las librerias necesarias
import utils as u
import json
import Tarea as t
import sklearn as skl


def generarReport(listadoTareas=None): # TODO: Terminar método
    """ Función que genera un reporte sobre las tareas pendientes y las realizadas en orden de prioridad. """
    if listadoTareas is None:
        listadoTareas = {}

    tareasSinCompletar = {}
    tareasCompletadas = {}

    for k, v in list(listadoTareas.items()):
        if v.completada:
            tareasCompletadas[k] = v
        else:
            tareasSinCompletar[k] = v
        if v.subTareas:
            generarReport(v.subTareas)

    dictFinal = tareasCompletadas|tareasSinCompletar
    return dictFinal