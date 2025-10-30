# Importación de las librerias necesarias

'''
    Agregar, editar, eliminar y listar tareas.
'''


'''
    Atributos Globales
'''
'''
    Prioridad de la tarea: 
        1 prioridad absoluta,
        2 prioridad media,
        3 prioridad baja
'''
OPCIONES_PRIORIDAD = [1, 2, 3]
listadoTareas = {}

# Clase Tarea para la creación, edicion y borrado de tareas.
class Tarea:

    # Atributos de la clase
    nombreTarea= str
    descripcion= str
    prioridad= int

    def __init__(self, nombreTarea, descripcion, prioridad):
        self.nombreTarea = nombreTarea
        self.descripcion = descripcion
        self.prioridad = prioridad

    def toString(self):
        return f'Tarea: {self.nombreTarea} \n\tDescripcion: {self.descripcion} \n\tPrioridad: {self.prioridad}\n'

    def setPrioridad(self, prioridad=-1):
        if prioridad not in OPCIONES_PRIORIDAD:
            self.prioridad = OPCIONES_PRIORIDAD[2]
        else:
            self.prioridad = prioridad

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
    return None


'''
    Funcion que lista todas las tareas si no se le introduce una prioridad.
    Si se le introduce una prioridad definida se muestran las  
'''
def listarTareas(prioridad=0):
    # Si se introduce una prioridad como parametro, mostramos todas las tareas y subtareas que tengan dicha prioridad
    if prioridad != 0 and prioridad in OPCIONES_PRIORIDAD:
        for id in listadoTareas:
            pass
    else: # mostramos todas las tareas
        pass


if __name__ == '__main__':

    listadoTareas = openJSON()
    opcion = -1
    while opcion != 0:
        opcion = int(input("Que operacion desea hacer: "))
        if opcion == 1:
            listarTareas()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 0:
            guardarJSON()
            print("Saliendo del programa TODO list.... ")
        else:
            print("Opcion no valida. ")