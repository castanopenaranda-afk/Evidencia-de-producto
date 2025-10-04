class Estudiante:
    def __init__(self, id, nombre, apellido, matricula, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula  # Número o código único de inscripción
        self.email = email

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre_completo()} | "
                f"Matrícula: {self.matricula} | Email: {self.email}")
    

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = {}  # Diccionario: id → Estudiante

    def registrar_estudiante(self, estudiante):
        if estudiante.id in self.estudiantes:
            print(f"Error: Ya existe un estudiante con ID {estudiante.id}.")
        elif any(e.matricula == estudiante.matricula for e in self.estudiantes.values()):
            print(f"Error: La matrícula '{estudiante.matricula}' ya está registrada.")
        else:
            self.estudiantes[estudiante.id] = estudiante
            print(f"Estudiante '{estudiante.nombre_completo()}' registrado en {self.nombre_curso}.")

    def listar_estudiantes(self):
        if not self.estudiantes:
            print(f"No hay estudiantes registrados en {self.nombre_curso}.")
        else:
            print(f"\n--- Estudiantes en {self.nombre_curso} ---")
            for estudiante in self.estudiantes.values():
                print(estudiante)

    def buscar_estudiante(self, id):
        return self.estudiantes.get(id, None)

    def actualizar_estudiante(self, id, nombre=None, apellido=None, matricula=None, email=None):
        if id not in self.estudiantes:
            print("Estudiante no encontrado.")
            return

        estudiante = self.estudiantes[id]

        # Validar unicidad de matrícula si se intenta cambiar
        if matricula is not None and matricula != estudiante.matricula:
            if any(e.matricula == matricula for e in self.estudiantes.values()):
                print(f"Error: La matrícula '{matricula}' ya está en uso.")
                return

        if nombre is not None:
            estudiante.nombre = nombre
        if apellido is not None:
            estudiante.apellido = apellido
        if matricula is not None:
            estudiante.matricula = matricula
        if email is not None:
            estudiante.email = email

        print(f"Estudiante ID {id} actualizado.")

    def eliminar_estudiante(self, id):
        if id in self.estudiantes:
            eliminado = self.estudiantes.pop(id)
            print(f"Estudiante '{eliminado.nombre_completo()}' eliminado del curso.")
        else:
            print("Estudiante no encontrado.")       


 # Crear curso
curso = Curso("Programación Avanzada")

# Crear estudiantes
e1 = Estudiante(1, "María", "Gómez", "MAT2025-001", "maria.gomez@universidad.edu")
e2 = Estudiante(2, "Luis", "Fernández", "MAT2025-002", "luis.fernandez@universidad.edu")

# Registrar estudiantes
curso.registrar_estudiante(e1)
curso.registrar_estudiante(e2)

# Listar estudiantes
curso.listar_estudiantes()

# Actualizar un estudiante
curso.actualizar_estudiante(1, email="maria.nueva@universidad.edu")

# Buscar un estudiante
est = curso.buscar_estudiante(2)
if est:
    print("\nEstudiante encontrado:", est)

# Intentar registrar con matrícula duplicada
e3 = Estudiante(3, "Ana", "López", "MAT2025-001", "ana.lopez@universidad.edu")
curso.registrar_estudiante(e3)  # ← Esto mostrará error

# Eliminar un estudiante
curso.eliminar_estudiante(1)

# Listar de nuevo
curso.listar_estudiantes()           