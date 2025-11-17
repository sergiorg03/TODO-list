# Proyecto ToDo List - Sergio Rodríguez Geniz 

Aplicación de consola escrita en **Python** para gestionar tareas de manera sencilla y predecible.
Las tareas introducidas se almacenan en un archivo **JSON**, lo que permite conservar información en ejectuciones diferentes. 

## - Características principales
- Añadir tareas.
- Editar tareas.
- Eliminar tareas. 
- Listar las tareas creadas.
- Buscar tareas por categoria o por prioridad.

## - Estructura del proyecto
```
TODO-List/
│── main.py
│── data_handler.py
│── reports.py
│── Tarea.py
│── utils.py
│── README.md
└── tareas.json
```

## ¿Cómo ejecutar el proyecto?
1. Es necesario tener instalado **Python 3.10+**. 
2. Clona este repositorio pegando el siguiente comando en la terminal si tienes instalado Git en tu dispositivo:  `git clone https://github.com/sergiorg03/TODO-list.git`  
o en su defecto descarga el repositorio desde el botón `Code/Download Zip`.

3. Entra en la carpeta del proyecto desde la **CMD**. 
4. Ejecuta el comando `python main.py`

## Funcionalidades del **JSON**
El archivo **Tareas.json** se carga al iniciar la app.
- Si existe: Se lee el archivo y se convierten las tareas a un diccionario para poder tratarlas.
- Si no existe: Se crea el archivo vacio automáticamente. 

## Funcionalidades clave
### Añadir tareas.
El programa permite al usuario crear tareas nuevas.

### Editar tareas.
El programa permite al usuario editar una tarea creada anteriormente. 

### Eliminar tareas.
El programa permite al usuario eliminar tareas indicadas mediante un ***ID***, si el ***ID*** indicado no existe se le indicará al usuario que el valor introducido no existe y seguidamente se le solicitará otro ***ID***. 

### Listar tareas.
El programa permite al usuario mostrar todas las tareas creadas completadas y sin completar.

### Buscar tareas.
El programa permite al usuario buscar tareas de dos formas diferentes:
- Mediante la **Categoria**: Se le pedirá al usuario una categoria y se le mostraran todas las tareas que tengan dicha categoria. Si no existen tareas con dicha categoria se le mostrará un mensaje de error diciendo que no hay tareas con la categoria especificada.
- Mediante la **Prioridad**: Se le solicitará al usuario una prioridad valida y seguidamente se le mostraran todas las tareas que tengan dicha prioridad. Si no existen tareas con dicha prioridad se le mostrará un mensaje de error diciendo que no hay tareas con la prioridad especificada.

# Errores comunes.
### KeyError
Este error se producia cuando el usuario intentaba realizar el borrado o la edición de una tarea creada anteriormente y saltaba una excepción sobre la clave introducida informando que esta no existia.  

***Solución:***  
Este error saltaba cuando las claves introducidas eran de diferentes tipos (e.g: clave (str), valor introducido por el usuario (int)) y fue solucionado realizando el parseo de todos los datos introducidos al mismo tipo. E.g: str.

### Modificación del ultimo item del diccionario de tareas
Este error se producia cuando al introducir una nueva tarea el método lastSetID() devolvia el mismo ID al crear la nueva tarea.  

***Solución:***  
Este error fue solucionado leyendo el último ID de la lista, comprobando que este fuera un número y devolviendo el valor + 1. 

### JSONDecodeError
Este error se producia cuando intentabamos leer el archivo de guardado de las tareas pero este no existia o se encontraba en estado vacio.  

***Solución:***   
Para solucionar este error realizamos una comprobación previa antes de leer el archivo. Si este no existia, estaba corrupto o estaba vacio, creabamos un nuevo archivo vacio y devolviamos un diccionario vacio para comenzar a crear tareas sin problemas.

# Licencia.
Este proyecto es de uso educativo y personal.

# Contribuciones.
El proyecto fue realizado solamente por **Sergio Rodríguez Geniz**.

# Contacto.
Si deseas contactar conmigo para aclarar dudas o funcionalidades de la app:
- [sergiorodriguezprofesional@gmail.com](mailto:sergiorodriguezprofesional@gmail.com)
- [srodgen0910@g.educaand.es](mailto:srodgen0910@g.educaand.es)