'''
    Prioridad de la tarea:
        1 prioridad absoluta,
        2 prioridad media,
        3 prioridad baja
'''
OPCIONES_PRIORIDAD = [1, 2, 3]

class Utils:
    '''    instancia= None

    def __init__(self):
        pass

    def getInstance(self):
        if instancia is None:
            instancia =  Utils()

        return instancia
'''

'''
    Método que guarda el JSON al final cerrar la aplicación con todas las modificaciones realizadas en el mismo.
'''
def guardarJSON():
    pass

'''
    Método que abre el JSON al inicio de la aplicación y guarda todos los datos en una lista (listadoTareas) 
    para poder realizar todas las modificaciones necesarias.
'''
def openJSON():
    return ""

'''
    Método que lee cual es el último ID asignado y asigna nuevos IDs
'''

def lastSetID():
    global ultimoID # Utilizamos la variable global
    # Si la variable último ID es -1 leerá el archivo JSON y buscará el último ID asignado
    if ultimoID == -1:
        pass
    else: # Si la variable es diferente a -1, es decir, ha encontrado el último ID asignado, le sumamos uno y lo devolvemos
        ultimoID += 1
    return ultimoID

'''
    Funcion que lista todas las tareas si no se le introduce una prioridad.
    Si se le introduce una prioridad definida se muestran las  
'''
def listarTareas(prioridad=0, listadoTareas={}):
    # Si se introduce una prioridad como parametro, mostramos todas las tareas y subtareas que tengan dicha prioridad
    if prioridad != 0 and prioridad in OPCIONES_PRIORIDAD:
        for id in listadoTareas:
            pass
    else: # mostramos todas las tareas
        pass


'''
    Método que genera un reporte sobre las tareas pendientes, las realizadas en orden de prioridad.
'''
def generarReport():
    pass

'''
    Método que permite al usuario añadir una nueva tarea
'''
def addTarea(ultimoIDUsado: int):
    pass

