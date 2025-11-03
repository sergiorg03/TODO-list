# Importación de las librerias necesarias
import json
import os
import Tarea as t
import utils as u
import sklearn as skl

_fichero = 'Tareas.json'

def guardarJSON(listadoTareas=None):
    """ Función que guarda el JSON al final cerrar la aplicación con todas las modificaciones realizadas en el mismo."""
    listadoTareasJSON = {k: v.to_dict() for k, v in listadoTareas.items()}

    with open(_fichero, 'w', encoding="utf8") as file:
        json.dump(listadoTareasJSON, file, ensure_ascii=False, indent=4)

def openJSON():
    """ Función que abre el JSON al inicio de la aplicación y guarda todos los datos en una lista (listadoTareas)
    para poder realizar todas las modificaciones necesarias."""
    listado = None
    try:
        if os.path.isfile(_fichero):
            with open(_fichero, 'r', encoding="utf8") as file:
                datos = json.load(file)

            listado = {k: t.Tarea(**v) for k, v in datos.items()}
    except FileNotFoundError:
        with open(_fichero, 'w', encoding="utf8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
        return None
    return listado if listado is not None else print("El fichero de tareas no existe. ")

def generarReport():
    """ Función que genera un reporte sobre las tareas pendientes, las realizadas en orden de prioridad. """
    pass

def addTarea(ultimoIDUsado: int):
    """ Función que permite al usuario añadir una nueva tarea. """
    pass