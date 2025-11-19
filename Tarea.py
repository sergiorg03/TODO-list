# Importamos las librerias y clases necesarias
import utils as u

# Clase Tarea para la creación, edicion y borrado de tareas.
class Tarea:

    def __init__(self, nombreTarea, descripcion, categoria, prioridad=3, completada=False):
        self.nombreTarea = nombreTarea
        self.descripcion = descripcion
        self.categoria = categoria if categoria is not None else {}
        self.prioridad = prioridad
        self.completada = completada


    def __str__(self):
        categorias = u.getCategorias(self) if self.categoria else "No tiene subcategorias. "
        return f'Nombre: {self.nombreTarea} \n\tDescripcion: {self.descripcion} \n\tPrioridad: {self.prioridad} \n\tCompletada: {"Si" if self.completada else "No"} \n\tCategorias: {categorias} '

    def to_dict(self):
        '''
            Función que convierte la tarea en una cadena para guardarla en un JSON.
        '''
        sub_cat = {}
        if self.categoria: # No es None y contiene datos
            for clave, v in self.categoria.items():
                if isinstance(v, Tarea):  # Comprobamos que el valor obtenido sea una instancia de la clase Tarea
                    sub_cat[clave] = v.to_dict()
                else:  # si ya es un diccionario, lo dejamos igual
                    sub_cat[clave] = v

        return {
            "nombreTarea": self.nombreTarea,
            "descripcion": self.descripcion,
            "categoria": sub_cat,
            "prioridad": self.prioridad,
            "completada": self.completada
        }