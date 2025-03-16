Documentación de los Principales Cambios
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
