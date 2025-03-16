# GestorTareas
 Gestor de tareas en Python
 Documentación del Gestor de Tareas en Python
 Descripción
   Este programa en escrito en Python permite al usuario administrar tareas pendientes de manera interactiva. El usuario puede agregar nuevas tareas, listarlas, marcarlas como completadas y salir del programa a través de un menú de opciones.
 Características
     •	Creación de tareas con título y descripción.
     •	Listado de tareas con su estado.
     •	Marcado de tareas como completadas mediante entrada del usuario.
     •	Interfaz interactiva en consola.
 Estructura del Código
   El código se organiza en dos clases y una función principales para la ejecución del programa:
 1. Clase Tarea
   Representa una tarea individual con los siguientes atributos y métodos:
     Atributos:
     •	titulo (str): Nombre de la tarea.
     •	descripcion (str): Descripción de la tarea.
     •	completada (bool): Indica si la tarea está completada (que por defecto es False).
   Métodos:
     •	__init__(self, titulo, descripción): Constructor que inicia una tarea con título y descripción.
     •	marcar_completada(self): Cambia el estado de la tarea a completada.
     •	mostrar_info(self): Retorna una string con la información de la tarea.
 2. Clase GestorTareas
   Gestiona una lista de tareas y proporciona métodos para interactuar con ellas.
   Atributos:
     •	tareas (list): Lista de objetos Tarea.
   Métodos:
     •	__init__(self): Inicia una lista vacía de tareas.
     •	agregar_tarea(self, titulo, descripcion): Crea y añade una nueva tarea a la lista.
     •	listar_tareas(self): Muestra todas las tareas registradas con su estado.
     •	completar_tarea(self): Permite al usuario seleccionar y completar una tarea mediante input().
 3. Función menu()
   Controla la ejecución del programa y presenta un menú interactivo al usuario.
   Opciones del menú:
     1.	Agregar tarea: Permite ingresar un título y descripción para una nueva tarea.
     2.	Listar tareas: Muestra todas las tareas registradas junto con su estado.
     3.	Completar tarea: Permite seleccionar una tarea y marcarla como completada.
     0.	Salir: Termina la ejecución del programa.
 Uso del Programa
   Ejecutar el programa mostrará el siguiente menú interactivo:
 
 --- GESTOR DE TAREAS ---
 1. Agregar tarea
 2. Listar tareas
 3. Completar tarea
 0. Salir
 Seleccione una opción:
   El usuario puede seleccionar una opción ingresando un número.

Principales Cambios
  Esta actualización del programa introduce herencia en la gestión de tareas permitiendo clasificar las tareas en Tareas Personales y Tareas de Trabajo. Estos elementos complementan la primera versión al hacer que las tareas sean más detalladas y especializadas.
Uso de Clases Derivadas
  Se utiliza la clase base ‘Tarea’ con los atributos y métodos comunes agregando dos subclases:
     •	tareaPersonal: Para tareas de uso personal, con un atributo extra de prioridad.
     •	tareaTrabajo: Para tareas laborales, con un atributo extra de fecha de entrega.
  Cada subclase sobrescribe el método mostrar_info() para personalizar la información mostrada.
Nuevos Atributos
  En la primera versión, todas las tareas eran iguales. Ahora, cuando el usuario crea una nueva tarea debe elegir entre:
     •	Tarea Personal (ingresando un nivel de prioridad).
     •	Tarea de Trabajo (ingresando una fecha de entrega).
Modificación de Métodos
  El método ‘mostrar_info()’, que antes solo mostraba título, descripción y estado de la tarea, ahora muestra:
     •	Prioridad en ‘tareaPersonal’.
     •	Fecha de entrega en ‘tareaTrabajo’.
