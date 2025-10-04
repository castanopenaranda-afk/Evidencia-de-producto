from datetime import datetime

class Tarea:
    def __init__(self, id, titulo, descripcion, fecha_limite):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite  # Esperamos un objeto datetime
        self.estado = "pendiente"  # Valores posibles: "pendiente", "completada"

    def completar(self):
        self.estado = "completada"

    def __str__(self):
        fecha_str = self.fecha_limite.strftime("%Y-%m-%d")
        return (f"ID: {self.id} | Título: {self.titulo} | Estado: {self.estado} | "
                f"Fecha límite: {fecha_str}\n  Descripción: {self.descripcion}")
    

class GestorTareas:
    def __init__(self):
        self.tareas = {}  # Diccionario: id → Tarea

    def agregar_tarea(self, tarea):
        if tarea.id in self.tareas:
            print(f"Error: Ya existe una tarea con ID {tarea.id}.")
        else:
            self.tareas[tarea.id] = tarea
            print(f"Tarea '{tarea.titulo}' agregada correctamente.")

    def listar_tareas(self, estado=None):
        tareas_filtradas = self.tareas.values()
        if estado:
            tareas_filtradas = [t for t in tareas_filtradas if t.estado == estado]

        if not tareas_filtradas:
            print("No hay tareas" + (f" con estado '{estado}'." if estado else "."))
        else:
            print(f"\n--- Lista de Tareas {'(' + estado + ')' if estado else ''} ---")
            for tarea in tareas_filtradas:
                print(tarea)
                print("-" * 50)

    def buscar_tarea(self, id):
        return self.tareas.get(id, None)

    def editar_tarea(self, id, titulo=None, descripcion=None, fecha_limite=None):
        if id not in self.tareas:
            print("Tarea no encontrada.")
            return

        tarea = self.tareas[id]
        if titulo is not None:
            tarea.titulo = titulo
        if descripcion is not None:
            tarea.descripcion = descripcion
        if fecha_limite is not None:
            tarea.fecha_limite = fecha_limite

        print(f"Tarea ID {id} actualizada.")

    def eliminar_tarea(self, id):
        if id in self.tareas:
            eliminada = self.tareas.pop(id)
            print(f"Tarea '{eliminada.titulo}' eliminada.")
        else:
            print("Tarea no encontrada.")

    def marcar_completada(self, id):
        tarea = self.buscar_tarea(id)
        if tarea:
            tarea.completar()
            print(f"Tarea '{tarea.titulo}' marcada como completada.")
        else:
            print("Tarea no encontrada.")   

from datetime import datetime

# Crear gestor
gestor = GestorTareas()

# Crear tareas
t1 = Tarea(1, "Estudiar POO", "Repasar conceptos de clases y objetos", datetime(2025, 4, 10))
t2 = Tarea(2, "Comprar víveres", "Ir al supermercado", datetime(2025, 4, 5))

# Agregar tareas
gestor.agregar_tarea(t1)
gestor.agregar_tarea(t2)

# Listar todas
gestor.listar_tareas()

# Marcar una como completada
gestor.marcar_completada(2)

# Listar solo pendientes
gestor.listar_tareas(estado="pendiente")

# Editar una tarea
gestor.editar_tarea(1, descripcion="Repasar POO y hacer ejercicios prácticos")

# Eliminar una tarea
gestor.eliminar_tarea(1)

# Listar de nuevo            