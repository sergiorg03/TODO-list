# Importamos las librerias y clases necesarias
import utils as u

# Clase Tarea para la creación, edicion y borrado de tareas.
class Tarea:

    # Atributos de la clase
    nombreTarea= str
    descripcion= str
    categoria= str
    prioridad= int
    completada= bool
    subTareas= {}

    def __init__(self, nombreTarea, descripcion, categoria, prioridad=3, completada=False, subTareas=None):
        self.nombreTarea = nombreTarea
        self.descripcion = descripcion
        self.categoria = categoria
        self.prioridad = prioridad
        self.completada = completada
        self.subTareas = subTareas if subTareas is not None else {}

    def toString(self):
        return f'Nombre: {self.nombreTarea} \n\tDescripcion: {self.descripcion} \n\tPrioridad: {self.prioridad}\n'

    def setPrioridad(self, prioridad=-1):
        if prioridad not in u.OPCIONES_PRIORIDAD:
            self.prioridad = u.OPCIONES_PRIORIDAD[len(u.OPCIONES_PRIORIDAD)-1]
        else:
            self.prioridad = prioridad

    def to_dict(self):
        ''' Función que convierte la tarea en una cadena. '''
        sub_tarea = {}
        if self.subTareas: # No es None y contiene datos
            for clave, v in self.subTareas.items():
                if isinstance(v, Tarea):  # Comprobamos que el valor obtenido sea una instancia de la clase Tarea
                    sub_tarea[clave] = v.to_dict()
                else:  # si ya es un diccionario, lo dejamos igual
                    sub_tarea[clave] = v

        return {
            "nombreTarea": self.nombreTarea,
            "descripcion": self.descripcion,
            "categoria": self.categoria,
            "prioridad": self.prioridad,
            "completada": self.completada,
            "subTareas": sub_tarea
        }