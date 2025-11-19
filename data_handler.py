# Importación de las librerias necesarias
import json
import os
import Tarea as t
import utils as u
import re as r

_fichero = 'tareas.json'

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

        if not os.path.exists(_fichero): # No existe el fichero, lo creamos
            #print(f"El fichero {_fichero} no existe")
            with open(_fichero, "w", encoding="utf8") as file:
                json.dump({}, file, ensure_ascii=False, indent=4)
            return {}

        try:
            with open(_fichero, "r", encoding="utf8") as file: # Abrimos el archivo e intentamos leerlo. Si no contiene nada devolvemos un diccionario vacio para comenzar a añadir tareas.
                contenido = file.read().strip()
                if not contenido: # Comprobamos que el archivo no este vacio
                    #print("El archivo está vacio.")
                    return {}

                datos = json.loads(contenido)
                listado = {k: u.from_dict(data=v) for k, v in datos.items()}

        except json.JSONDecodeError:
            print("El archivo JSON está corrupto. ")
            listado = {}
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
                "¿Desea añadir una subcategoria más? \n\t1 --> Desea añadir una subcategoria más. \n\t0 --> No desea añadir más subcategorias. ").strip())
            if op2 == 1:
                subcat = input("Introduce la subcategoria de la tarea: ").strip()
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
    nombreTarea = input(f"Introduce el nombre de la tarea: \n").strip()
    desc = input("Introduce una descripción de la tarea: \n").strip()
    cat = addSubCategorias()
    prioridad = input(
        "Introduce la prioridad de la tarea (Valores permitidos: 1, 2, 3 siendo el 1 la tarea con más prioridad y la 3 la que menos): \n").strip()
    while not u.prioridadCorrecta(prioridad):
        prioridad = input("El valor de prioridad introducido es incorrecto, introduce un valor de prioridad entre los valores 1 y 3: \n").strip()
    completada = input("Introduce si la tarea está completada o no: \n\tSi --> La tarea está completada \n\tNo --> La tarea no está completada\n").strip()
    while not u.completadaCorrecta(completada):
        completada = input("El valor introducido es incorrecto, introduzca un valor correcto: \n\tSi --> La tarea está completada \n\tNo --> La tarea no está completada\n").strip()

    t1 = t.Tarea(nombreTarea=nombreTarea, descripcion=desc, categoria=cat, prioridad=int(prioridad), completada= True if completada.lower() == "si" else False)

    listadoTareas[ultimoIDUsado] = t1

def eliminarTarea(listadoTareas, IDTareaEliminar:str):
    """
        Función que elimina una tarea indicada mediante el ID de tarea.

        :param listadoTareas: Listado de tareas.
        :param IDTareaEliminar: ID de la tarea a eliminar.
    """
    if IDTareaEliminar in listadoTareas:
        listadoTareas.pop(IDTareaEliminar)
        print("Tarea eliminada correctamente... \n")
    else: 
        print("No se pudo eliminar la tarea. ")

def editCategorias(categorias:dict):
    print() # Separadores
    for clave, valorCategoria in list(categorias.items()):
        print(f"ID: {clave} --> {valorCategoria}")

    print() # Separadores

    op = -2
    while op != -1:
        try:
            op = int(input('Introduzca el ID de la categoria a editar o -1 para salir: \n').strip())

            if u.idInLista(listaTareas=categorias, idTarea=op):
                cat = input("Introduce el nuevo valor de la categoria: \n").strip()
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

    if listadoTareas and u.idInLista(listaTareas=listadoTareas, idTarea=idTareaEditar):
        opcion = -1
        while opcion != 0:
            try:
                opcion = int(input("Que datos desea editar de la tarea: \n\t1 --> El nombre. \n\t2 --> La descripción. \n\t3 --> La categoria. \n\t4 --> La prioridad. \n\t5 --> Está completada. \n\t0 --> Salir. ").strip())

                if opcion == 1: # Nombre
                    listadoTareas[idTareaEditar].nombreTarea = input("Introduce el nuevo nombre de la tarea: \n").strip()
                elif opcion == 2: # Descripcion
                    listadoTareas[idTareaEditar].descripcion = input("Introduce la descripción de la tarea: \n").strip()
                elif opcion == 3: # Categoria
                    listadoTareas[idTareaEditar].categoria = editCategorias(listadoTareas[idTareaEditar].categoria)
                elif opcion == 4: # Prioridad
                    try:
                        prio = int(input("Introduce la nueva prioridad de la tarea: \n").strip())
                        if prio in u.OPCIONES_PRIORIDAD:
                            listadoTareas[idTareaEditar].prioridad = prio
                        else:
                            print(f"La prioridad no se ha podido modificar ya que el valor {prio} no está en las opciones de prioridad establecidas (1, 2, 3).")
                    except ValueError:
                        print("Opcion no valida. ")
                elif opcion == 5: # Completada
                    completa = input("Introduce si se ha completado la tarea: \n\tSi --> Si la tarea se ha completado. \n\tNo --> Si la tarea no se ha completada\n").strip()
                    while not u.completadaCorrecta(completa):
                        completa = input("El valor introducido no es correcto, introduzca un valor correcto: \n").strip()
                    listadoTareas[idTareaEditar].completa = True if completa.lower() == "si" else False
                elif opcion == 0: # Salir
                    print("Saliendo de la edición de la tarea. ")
                else:
                    print("Opcion no valida. Por favor introduzca una opción correcta. ")
            except ValueError:
                print("Opcion no valida. ")

    else: 
        print("La lista de tareas está vacía o el ID introducido no existe en la lista. ")

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
    
    if categoria: # Buscamos por categoria
        categoria_upper = categoria.upper() 
        # Creamos el diccionario de tareas
        tareas = {
            clave: tarea 
            for clave, tarea in listadoTareas.items() 
            if tarea.categoria and any(val.upper() == categoria_upper for val in tarea.categoria.values())
        }
    else: 
        # No se introduce la categoria a buscar por lo que se realiza la busqueda por prioridades
        tareas = {
            clave: tarea 
            for clave, tarea in listadoTareas.items() 
            if tarea.prioridad == prioridad
        }
    return tareas if tareas else {"Error": "No hay tareas."}


