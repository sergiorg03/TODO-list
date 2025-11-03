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

            listado = {k: u.from_dict(data=v) for k, v in datos.items()}
    except FileNotFoundError:
        with open(_fichero, 'w', encoding="utf8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
        return None
    return listado if listado is not None else print("El fichero de tareas no existe. ")

def generarReport():
    """ Función que genera un reporte sobre las tareas pendientes, las realizadas en orden de prioridad. """
    pass

def addTarea(ultimoIDUsado: int= 0, listadoTareas=None):
    """ Función que permite al usuario añadir una nueva tarea. """
    nombreTarea = input(f"Introduce el nombre de la tarea: \n")
    desc = input("Introduce una descripción de la tarea: \n")
    cat = input("Introduce una categoria de la tarea: \n")
    prioridad = input(
        "Introduce la prioridad de la tarea (Valores permitidos: 1, 2, 3 siendo el 1 la tarea con más prioridad y la 3 la que menos): \n")
    while not u.prioridadCorrecta(prioridad):
        prioridad = input("El valor de prioridad introducido es incorrecto, introduce un valor de prioridad entre los valores 1 y 3: \n")
    completada = input("Introduce si la tarea está completada o no: \n\tSi --> La tarea está completada \n\tNo --> La tarea no está completada\n")
    while not u.completadaCorrecta(completada):
        completada = input("El valor introducido es incorrecto, introduzca un valor correcto: \n\tSi --> La tarea está completada \n\tNo --> La tarea no está completada\n")

    t1 = t.Tarea(nombreTarea=nombreTarea, descripcion=desc, categoria=cat, prioridad=prioridad, completada= True if completada.lower() == "si" else False, subTareas={})

    listadoTareas[ultimoIDUsado] = t1

def eliminarTarea(listadoTareas, IDTareaEliminar:int):
    ''' Función que elimina una tarea indicada mediante el ID de tarea '''
    for clave, valor in list(listadoTareas.items()):
        if clave == IDTareaEliminar:
            listadoTareas.pop(IDTareaEliminar)
        else:
            if valor.subTareas:
                eliminarTarea(valor.subTareas, IDTareaEliminar)