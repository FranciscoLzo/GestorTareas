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

class tareaPersonal(Tarea):
    def __init__(self, titulo, descripcion, prioridad):     # Constructor de tareaPersonal que añade el atributo de prioridad
        super().__init__(titulo, descripcion)
        self.prioridad = prioridad  # Nuevo atributo exclusivo

    def mostrar_info(self):         #Sobrescribimos mostrar_info() para incluir la prioridad
        info_base = super().mostrar_info()
        return f"{info_base}Prioridad: {self.prioridad}\n"

class tareaTrabajo(Tarea):
    def __init__(self, titulo, descripcion, fecha_entrega): # Constructor de tareaTrabajo que añade el atributo de fecha_entrega
        super().__init__(titulo, descripcion)
        self.fecha_entrega = fecha_entrega  # Nuevo atributo exclusivo

    def mostrar_info(self):         # Muestra la informacion de la tarea, titulo, descripcion y estado
                                    # Sobrescribimos mostrar_info() para incluir la fecha de entrega
        info_base = super().mostrar_info()
        return f"{info_base}Fecha de entrega: {self.fecha_entrega}\n"

class gestorTareas:
    def __init__(self):             # Constructor de la clase GestorTareas
        self.tareas = []

    def agregar_tarea(self): # Permite al usuario agregar una tarea seleccionando el tipo
        print("\nSeleccione el tipo de tarea:")
        print("1. Tarea Personal")
        print("2. Tarea de Trabajo")

        opcion = input("Ingrese una opción: ")

        titulo = input("Título de la tarea: ")
        descripcion = input("Descripción de la tarea: ")

        if opcion == "1":
            prioridad = input("Ingrese la prioridad (Alta, Media, Baja): ")
            nueva_tarea = tareaPersonal(titulo, descripcion, prioridad)
        elif opcion == "2":
            fecha_entrega = input("Ingrese la fecha de entrega (DD/MM/AAAA): ")
            nueva_tarea = tareaTrabajo(titulo, descripcion, fecha_entrega)
        else:
            print("Opción inválida. La tarea no se agregó.")
            return

        self.tareas.append(nueva_tarea)
        print("\nTarea agregada con éxito.\n")

    def listar_tareas(self):    # Muestra todas las tareas existentes mediante bucle for
        if not self.tareas:     # En caso de no haber nignuna lanza un mensaje al usuario
            print("\nNo hay tareas registradas.")
        else:
            print("\n--- Lista de tareas ---\n")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea.mostrar_info()}")

    def completar_tarea(self):  # Para completar una tarea y evitar valores invalidos se utiliza try, controlando los inputs del usuario
        if not self.tareas:     # en caso de no haber tareas registradas se manda un mensaje al usuario
            print("\nNo hay tareas para completar.")
            return

        self.listar_tareas()
        
        try:
            indice = int(input("\nIngrese el número de la tarea aque desee completar: ")) - 1
            if 0 <= indice < len(self.tareas):
                self.tareas[indice].marcar_completada()
                print(f"\nTarea '{self.tareas[indice].titulo}' completada.\n")
            else:
                print("\nNúmero inválido.")
        except ValueError:
            print("\nIntroduzca un número válido.")

def menu():     # Funciín para el menu interactivo
    gestor = gestorTareas()

    while True:        # Bucle while True para iniciar siempre el menu
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor.agregar_tarea()
        elif opcion == "2":
            gestor.listar_tareas()
        elif opcion == "3":
            gestor.completar_tarea()
        elif opcion == "0":
            print("Cerrando gestor...\n")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
