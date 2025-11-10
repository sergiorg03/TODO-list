# Importacion de las librerias y clases necesarias
import Tarea as t

'''
    Prioridad de la tarea:
        1 prioridad absoluta,
        2 prioridad media,
        3 prioridad baja
'''
OPCIONES_PRIORIDAD = [1, 2, 3]
_fichero = 'Tareas.json'
ultimoID:int = -1

class Utils:
    _instancia= None

    # Constructor de la clase
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia


def lastSetID(listadoTareas):
    """
        Función que lee cuál es el último ID asignado y asigna nuevos IDs.

        :param
            listadoTareas: Listado de tareas en las que busca el último ID

        :returns
            Integer: Devuelve el ultimo ID usado + 1 para asignar directamente.
    """
    # El último ID que devuelve no se ha usado todavia
    global ultimoID # Utilizamos la variable global
    # Si la variable último ID es -1 leerá el archivo JSON y buscará el último ID asignado
    if ultimoID == -1:
        ultimoID = next(reversed(listadoTareas)) if listadoTareas else 0
    return int(ultimoID )+1

def listarTareas(listadoTareas=None, prioridad=0, nivel=0):
    """
        Función que lista todas las tareas si no se le introduce una prioridad.
        Si se le introduce una prioridad definida se muestran las tareas con dicha prioridad.

        :param listadoTareas: Listado de tareas a mostrar
        :param prioridad: Prioridad de las tareas a mostrar
        :param nivel: Nivel de tabulación para subcategorias

        :returns String: Devuelve una cadena para mostrar directamente
    """
    cadToReturn = ""
    indent = "-- " * nivel

    if listadoTareas is None: # Comprobamos que no se None
        listadoTareas = {}

    # Si se introduce una prioridad como parametro, mostramos todas las tareas con dicha prioridad
    if prioridadCorrecta(prioridad):
        for key, value in listadoTareas.items():
            if hasattr(value, '__str__'): # El objeto es de tipo Tarea
                if value.prioridad == prioridad: # Comprobamos la prioridad
                    cadToReturn += f"{indent}ID: {key} --> {value.__str__()}\n" # Lo añadimos para devolverla al final

            elif isinstance(value, dict): # El objeto es de tipo diccionario
                if value.get("prioridad") == prioridad: #comprobamos la prioridad
                    cad = (f'Nombre: {value.get("nombreTarea", "Sin nombre")} \n\t'
                           f'Descripcion: {value.get("descripcion", "Sin descripción")} \n\t'
                           f'Prioridad: {value.get("prioridad", 0)}\n')
                    cadToReturn += f"{indent}ID: {key} -> {cad}\n"

    else: # mostramos todas las tareas
        for key, value in listadoTareas.items():
            if hasattr(value, '__str__'): # El objeto es de tipo Tarea
                cadToReturn += f"{indent}ID: {key} --> {value.__str__()}\n"  # Lo añadimos para devolverla al final
            elif isinstance(value, dict): # El objeto es de tipo diccionario
                cad = (f'Nombre: {value.get("nombreTarea", "Sin nombre")} \n\t'
                       f'Descripcion: {value.get("descripcion", "Sin descripción")} \n\t'
                       f'Prioridad: {value.get("prioridad", 0)}\n')
                cadToReturn += f"{indent}ID: {key} -> {cad}\n"

    return cadToReturn

def from_dict(data):
    '''
        Función que crea tareas a partir del diccionario leido del JSON.

        :param data: Cadena que contiene los datos leidos del JSON.

        :returns Tarea: Devuelve una tarea con sus subtareas.
    '''
    tarea = t.Tarea(
        data["nombreTarea"],
        data["descripcion"],
        data["categoria"],
        data["prioridad"],
        data["completada"]
    )

    return tarea

def prioridadCorrecta(prioridad):
    '''
        Función que devuelve si la prioridad introducida es correcta.

        :param prioridad: Prioridad introducida a comprobar si es correcta.

        :returns Boolean: True si la prioridad introducida es correcta. False si no.
    '''
    try:
        value = int(prioridad) in OPCIONES_PRIORIDAD
    except ValueError:
        value = False
    return value


def completadaCorrecta(completada:str):
    '''
        Función que comprueba si el valor introducido del campo "completada" es correcto.

        :param completada: Valor introducido a comprobar.

        :return:
            Boolean: Devuelve True si el valor introducido es "Si" o "No". False si no.
    '''
    if completada.lower() == "no" or completada.lower() == "si":
        return True
    return False


def isNumber(num):
    '''
        Función que devuelve True si el parametro introducido es un número. False si no lo es.

        :param num: Valor introducido a comprobar.
        :returns Boolean: Devuelve True si el valor introducido es un número entero o decimal. False si no.
    '''
    try:
        float(num)
        return True
    except ValueError:
        return False


def idInLista(listaTareas, idTarea):
    """
        Funcion que comprueba si un id introducido por parametro existe en la lista o no.

        :param listaTareas: Lista de tareas en la que comprobar el ID.
        :param idTarea: ID a comprobar.

        :return Boolean: True si el ID introducido existe en la lista. False si no.
    """
    for k, v in listaTareas.items():
        if k == idTarea:
            return True
    return False

def getCategorias(tarea:t.Tarea):
    '''
        Función que devuelve las categorías de una tarea.

        :return String: Cadena con las categorías disponibles.
    '''
    cad ="\n\t\t"
    for id, categoria in tarea.categoria.items():
        cad += f'ID: {id} --> : {categoria}\n\t\t'

    return cad