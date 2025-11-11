# Importación de las librerias necesarias
import json
import os
import Tarea as t
import utils as u
import re as r

_fichero = 'Tareas.json'

def guardarJSON(listadoTareas=None):
    """
        Función que guarda el JSON al final cerrar la aplicación con todas las modificaciones realizadas en el mismo.

        :param listadoTareas: Listado de tareas a guardar en el fichero JSON.
    """
    listadoTareasJSON = {k: v.to_dict() for k, v in listadoTareas.items()}

    with open(_fichero, 'w', encoding="utf8") as file:
        json.dump(listadoTareasJSON, file, ensure_ascii=False, indent=4)

def openJSON():
    """
        Función que abre el JSON al inicio de la aplicación y guarda todos los datos en una lista (listadoTareas)
        para poder realizar todas las modificaciones necesarias.
    """
    listado = None
    try:
        if os.path.isfile(_fichero):
            with open(_fichero, 'r', encoding="utf8") as file:
                datos = json.load(file)

            listado = {k: u.from_dict(data=v) for k, v in datos.items()}
    except FileNotFoundError:
        with open(_fichero, 'w', encoding="utf8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
    return listado if listado is not None else {}


def addSubCategorias():
    '''
        Función que devuelve un diccionario de las subcategorias de la tarea.
        :return: Diccionario con los valores de las subcategorias de la tarea.
    '''
    cat = {}
    cat1 = input("Introduce una categoria de la tarea: \n")
    cat[0] = cat1
    aux = []
    op2 = -1
    while op2 != 0:
        try:
            op2 = int(input(
                "¿Desea añadir una subcategoria más? \n\t1 --> Desea añadir una subcategoria más. \n\t0 --> No desea añadir más subcategorias. "))
            if op2 == 1:
                subcat = input("Introduce la subcategoria de la tarea: ")
                aux.append(subcat)
            elif op2 == 0:
                print("Saliendo... ")
        except ValueError:
            print("Valor no valido. ")

    cat.update((clave, valor) for clave, valor in enumerate(aux, start=1))
    return cat

def addTarea(ultimoIDUsado: int= 0, listadoTareas=None):
    """
        Función que permite al usuario añadir una nueva tarea.

        :param listadoTareas: Listado de tareas en la que añadiremos la nueva tarea.
        :param ultimoIDUsado: Id de la nueva tarea.
    """
    nombreTarea = input(f"Introduce el nombre de la tarea: \n")
    desc = input("Introduce una descripción de la tarea: \n")
    cat = addSubCategorias()
    prioridad = input(
        "Introduce la prioridad de la tarea (Valores permitidos: 1, 2, 3 siendo el 1 la tarea con más prioridad y la 3 la que menos): \n")
    while not u.prioridadCorrecta(prioridad):
        prioridad = input("El valor de prioridad introducido es incorrecto, introduce un valor de prioridad entre los valores 1 y 3: \n")
    completada = input("Introduce si la tarea está completada o no: \n\tSi --> La tarea está completada \n\tNo --> La tarea no está completada\n")
    while not u.completadaCorrecta(completada):
        completada = input("El valor introducido es incorrecto, introduzca un valor correcto: \n\tSi --> La tarea está completada \n\tNo --> La tarea no está completada\n")

    t1 = t.Tarea(nombreTarea=nombreTarea, descripcion=desc, categoria=cat, prioridad=prioridad, completada= True if completada.lower() == "si" else False)

    listadoTareas[ultimoIDUsado] = t1

def eliminarTarea(listadoTareas, IDTareaEliminar:str):
    """
        Función que elimina una tarea indicada mediante el ID de tarea.

        :param listadoTareas: Listado de tareas.
        :param IDTareaEliminar: ID de la tarea a eliminar.
    """
    for clave, tareas in list(listadoTareas.items()):
        if str(clave) == str(IDTareaEliminar):
            listadoTareas.pop(clave)
    print("Tarea eliminada correctamente... \n")

def editCategorias(categorias:dict):
    for clave, valorCategoria in list(categorias.items()):
        print(f"ID: {clave} --> {valorCategoria}")

    op = -2
    while op != -1:
        try:
            op = int(input('Introduzca el ID de la categoria a editar o -1 para salir: \n'))

            if str(op) in categorias:
                cat = input("Introduce el nuevo valor de la categoria: \n")
                categorias[op] = cat
                print("Categoria editada correctamente. ")
            elif op == -1:
                print("Saliendo...")
                break
            else: 
                print("El ID introducido no es correcto. ")
        except ValueError:
            print("Valor incorrecto. ")
    
    return categorias
        


def editarTarea(idTareaEditar:str, listadoTareas):
    """
        Función que edita la tarea indicada por parametro

        :param idTareaEditar: Id de la tarea a editar
        :param listadoTareas: Lista de tareas en las que buscar la tarea indicada para editarla.
    """
    if listadoTareas is None:
        listadoTareas = {}

    if listadoTareas:
        opcion = -1
        while opcion != 0:
            try:
                opcion = int(input("Que datos desea editar de la tarea: \n\t1 --> El nombre. \n\t2 --> La descripción. \n\t3 --> La categoria. \n\t4 --> La prioridad. \n\t5 --> Está completada. \n\t0 --> Salir. "))

                if opcion == 1: # Nombre
                    listadoTareas[idTareaEditar].nombreTarea = input("Introduce el nuevo nombre de la tarea: \n")
                elif opcion == 2: # Descripcion
                    listadoTareas[idTareaEditar].descripcion = input("Introduce la descripción de la tarea: \n")
                elif opcion == 3: # Categoria
                    listadoTareas[idTareaEditar].categoria = editCategorias(listadoTareas[idTareaEditar].categoria)
                elif opcion == 4: # Prioridad
                    try:
                        prio = int(input("Introduce la nueva prioridad de la tarea: \n"))
                        if prio in u.OPCIONES_PRIORIDAD:
                            listadoTareas[idTareaEditar].prioridad = prio
                        else:
                            print(f"La prioridad no se ha podido modificar ya que el valor {prio} no está en las opciones de prioridad establecidas (1, 2, 3).")
                    except ValueError:
                        print("Opcion no valida. ")
                elif opcion == 5: # Completada
                    completa = input("Introduce si se ha completado la tarea: \n\tSi --> Si la tarea se ha completado. \n\tNo --> Si la tarea no se ha completada\n")
                    while not u.completadaCorrecta(completa):
                        completa = input("El valor introducido no es correcto, introduzca un valor correcto: \n")
                    listadoTareas[idTareaEditar].completa = True if completa.lower() == "si" else False
                elif opcion == 0: # Salir
                    print("Saliendo de la edición de la tarea. ")
                else:
                    print("Opcion no valida. Por favor introduzca una opción correcta. ")
            except ValueError:
                print("Opcion no valida. ")

def buscarTarea(listadoTareas, categoria:str= "", prioridad:int= -1):
    """
        Función que realiza una búsqueda por categorías o por palabras clave por todas las tareas y las devuelve en forma de diccionario.

        :param listadoTareas: Lista de tareas en la que realizar la búsqueda.
        :param categoria: Categoria por la que buscar. Puede no introducirse.
        :param prioridad: Prioridad por la que buscar en todas las tareas. Puede no introducirse.

        :return:
            Devuelve un diccionario con las tareas encontradas con la misma categoria o que contienen la palabra clave.
    """
    tareas = {}
    if categoria: # Bucamos por categorias
        for clave, valor in listadoTareas.items():
            if valor.categoria:
                for key, val in valor.categoria.items():
                    if val == categoria:
                        tareas[clave] = valor
    else: # Buscamos por la prioridad
        for clave, valor in list(listadoTareas.items()):
            if valor.prioridad == prioridad:
                tareas[clave] = valor
    return tareas if tareas else {"Error": "No hay tareas."}


