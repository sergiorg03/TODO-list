# Importacion de las librerias y clases necesarias
import json
import os
import Tarea as t
import sklearn as skl

'''
    Prioridad de la tarea:
        1 prioridad absoluta,
        2 prioridad media,
        3 prioridad baja
'''
OPCIONES_PRIORIDAD = [1, 2, 3]
_fichero = 'Tareas.json'

class Utils:
    _instancia= None

    # Constructor de la clase
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia


def lastSetID():
    """ Función que lee cual es el último ID asignado y asigna nuevos IDs """
    global ultimoID # Utilizamos la variable global
    # Si la variable último ID es -1 leerá el archivo JSON y buscará el último ID asignado
    if ultimoID == -1:
        pass
    else: # Si la variable es diferente a -1, es decir, ha encontrado el último ID asignado, le sumamos uno y lo devolvemos
        ultimoID += 1
    return ultimoID

def listarTareas(prioridad=0, listadoTareas=None, nivel=0):
    ''' Funcion que lista todas las tareas si no se le introduce una prioridad.
        Si se le introduce una prioridad definida se muestran las tareas con dicha prioridad. '''
    cadToReturn = ""
    indent = "-- " * nivel

    if listadoTareas is None: # Comprobamos que no se None
        listadoTareas = {}

    # Si se introduce una prioridad como parametro, mostramos todas las tareas y subtareas que tengan dicha prioridad
    if prioridad != 0 and prioridad in OPCIONES_PRIORIDAD:
        for key, value in listadoTareas.items():
            if hasattr(value, 'toString'): # El objeto es de tipo Tarea
                if value.prioridad == prioridad: # Comprobamos la prioridad
                    cadToReturn += f"{indent}ID: {key} --> {value.toString()}\n" # Lo añadimos para devolverla al final
                if value.subTareas: #Comprobamos que tenga subtareas
                    cadToReturn += listarTareas(prioridad, value.subTareas, nivel + 1)
            elif isinstance(value, dict): # El objeto es de tipo diccionario
                if value.get("prioridad") == prioridad: #comprobamos la prioridad
                    cad = (f'Nombre: {value.get("nombreTarea", "Sin nombre")} \n\t'
                           f'Descripcion: {value.get("descripcion", "Sin descripción")} \n\t'
                           f'Prioridad: {value.get("prioridad", 0)}\n')
                    cadToReturn += f"{indent}ID: {key} -> {cad}\n"

                sub = value.get("subTareas", {})
                if sub:
                    cadToReturn += listarTareas(prioridad, sub, nivel + 1)
    else: # mostramos todas las tareas
        for key, value in listadoTareas.items():
            if hasattr(value, 'toString'): # El objeto es de tipo Tarea
                cadToReturn += f"{indent}ID: {key} --> {value.toString()}\n"  # Lo añadimos para devolverla al final
                if value.subTareas: #Comprobamos que tenga subtareas
                    cadToReturn += listarTareas(prioridad, value.subTareas, nivel + 1)
            elif isinstance(value, dict): # El objeto es de tipo diccionario
                cad = (f'Nombre: {value.get("nombreTarea", "Sin nombre")} \n\t'
                       f'Descripcion: {value.get("descripcion", "Sin descripción")} \n\t'
                       f'Prioridad: {value.get("prioridad", 0)}\n')
                cadToReturn += f"{indent}ID: {key} -> {cad}\n"

                sub = value.get("subTareas", {})
                if sub:
                    cadToReturn += listarTareas(prioridad, sub, nivel + 1)

    return cadToReturn

