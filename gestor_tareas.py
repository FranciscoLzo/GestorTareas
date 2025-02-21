class Tarea:
    def __init__(self, titulo, descripcion):    # Constructor para iniciar la tarea con los atributos 
        self.titulo = titulo                    # pendientes de titulo y descripcion
        self.descripcion = descripcion
        self.completada = False         #Estado inicial: Falso, no completada

    def marcar_completada(self):
        self.completada = True          # 

    def mostrar_info(self):             # Muestra la informacion de la tarea, titulo, descripcion y estado
        estado = "Completada" if self.completada else "Pendiente"
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {estado}\n"

class GestorTareas:
    def __init__(self):         
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):      # Crea una tarea nueva con los atributos (datos) proporcionados
        nueva_tarea = Tarea(titulo, descripcion)       # .append lo añade a la clase
        self.tareas.append(nueva_tarea)

    def listar_tareas(self):    # Muestra todas las tareas existentes mediante bucle for
        if not self.tareas:     # En caso de no haber nignuna lanza un mensaje al usuario
            print("No hay tareas registradas.")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea.mostrar_info()}")

    def completar_tarea(self):  # Para completar una tarea y evitar valores invalidos se utiliza try, controlando los inputs del usuario
        if not self.tareas:     # en caso de no haber tareas registradas se manda un mensaje al usuario
            print("No hay tareas para completar.")
            return
        self.listar_tareas()
        try:
            indice = int(input("Ingrese el número de tarea que desee completar: ")) - 1
            if 0 <= indice < len(self.tareas):
                self.tareas[indice].marcar_completada()
                print(f"Tarea '{self.tareas[indice].titulo}' completada.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Introduzca un número válido.")

def menu():             # Función para el menu interactivo
    gestor = GestorTareas() 

    while True:         # Bucle while True para iniciar siempre el menu
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":                          # Estructuras if-elif-else para controlar el flujo del menu
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            gestor.agregar_tarea(titulo, descripcion)
            print("Tarea agregada con éxito.")

        elif opcion == "2":
            print("\nLista de tareas:")
            gestor.listar_tareas()

        elif opcion == "3":
            gestor.completar_tarea()

        elif opcion == "0":
            print("Cerrando gestor...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()      # Ejecuta el menu de opciones