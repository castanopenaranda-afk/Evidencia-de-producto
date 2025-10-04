class Libro:
    def __init__(self, id, titulo, autor, año_publicacion, genero):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.genero = genero

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Año: {self.año_publicacion} | Género: {self.genero}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Usamos un diccionario para acceso rápido por ID

    def agregar_libro(self, libro):
        self.libros[libro.id] = libro

    def editar_libro(self, id, titulo=None, autor=None, año_publicacion=None, genero=None):
        if id in self.libros:
            libro = self.libros[id]
            if titulo is not None:
                libro.titulo = titulo
            if autor is not None:
                libro.autor = autor
            if año_publicacion is not None:
                libro.año_publicacion = año_publicacion
            if genero is not None:
                libro.genero = genero
        else:
            print("Libro no encontrado.")

    def eliminar_libro(self, id):
        if id in self.libros:
            del self.libros[id]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    def listar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros.values():
                print(libro)



   # Crear biblioteca
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro(1, "Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico")
libro2 = Libro(2, "1984", "George Orwell", 1949, "Distopía")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Listar libros
biblioteca.listar_libros()

# Editar un libro
biblioteca.editar_libro(1, año_publicacion=1968)

# Eliminar un libro
biblioteca.eliminar_libro(2)

# Listar de nuevo
biblioteca.listar_libros()             