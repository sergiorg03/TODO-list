# Importamos las librerias y clases necesarias
import Utils as u

# Clase Tarea para la creación, edicion y borrado de tareas.
class Tarea:

    # Atributos de la clase
    nombreTarea= str
    descripcion= str
    categoria= str
    prioridad= int
    completada= bool

    def __init__(self, nombreTarea, descripcion, categoria, prioridad=3, completada=False):
        self.nombreTarea = nombreTarea
        self.descripcion = descripcion
        self.categoria = categoria
        self.prioridad = prioridad
        self.completada = completada

    def toString(self):
        return f'Tarea: {self.nombreTarea} \n\tDescripcion: {self.descripcion} \n\tPrioridad: {self.prioridad}\n'

    def setPrioridad(self, prioridad=-1):
        if prioridad not in u.OPCIONES_PRIORIDAD:
            self.prioridad = u.OPCIONES_PRIORIDAD[len(u.OPCIONES_PRIORIDAD)-1]
        else:
            self.prioridad = prioridad