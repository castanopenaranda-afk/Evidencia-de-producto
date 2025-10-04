class Pelicula:
    def __init__(self, id, titulo, director, genero, duracion):
        self.id = id
        self.titulo = titulo
        self.director = director
        self.genero = genero
        self.duracion = duracion  # duración en minutos (int)

    def duracion_formateada(self):
        """Devuelve la duración en formato 'Xh Ym'."""
        horas = self.duracion // 60
        minutos = self.duracion % 60
        if horas > 0:
            return f"{horas}h {minutos}m"
        else:
            return f"{minutos}m"

    def __str__(self):
        return (f"ID: {self.id} | Título: {self.titulo} | Director: {self.director}\n"
                f"  Género: {self.genero} | Duración: {self.duracion_formateada()}")
    

class CatalogoCine:
    def __init__(self, nombre_cine="Cine Central"):
        self.nombre_cine = nombre_cine
        self.peliculas = {}  # Diccionario: id → Pelicula

    def agregar_pelicula(self, pelicula):
        if pelicula.id in self.peliculas:
            print(f"Error: Ya existe una película con ID {pelicula.id}.")
        else:
            self.peliculas[pelicula.id] = pelicula
            print(f"Película '{pelicula.titulo}' agregada al catálogo de {self.nombre_cine}.")

    def listar_peliculas(self):
        if not self.peliculas:
            print(f"El catálogo de {self.nombre_cine} está vacío.")
        else:
            print(f"\n--- Catálogo de {self.nombre_cine} ---")
            for pelicula in self.peliculas.values():
                print(pelicula)
                print("-" * 50)

    def buscar_pelicula(self, id):
        return self.peliculas.get(id, None)

    def editar_pelicula(self, id, titulo=None, director=None, genero=None, duracion=None):
        if id not in self.peliculas:
            print("Película no encontrada.")
            return

        pelicula = self.peliculas[id]
        if titulo is not None:
            pelicula.titulo = titulo
        if director is not None:
            pelicula.director = director
        if genero is not None:
            pelicula.genero = genero
        if duracion is not None:   
            if duracion > 0:
                pelicula.duracion = duracion
            else:
                print("La duración debe ser mayor a 0 minutos.")
                return

        print(f"Película ID {id} actualizada.")

    def eliminar_pelicula(self, id):
        if id in self.peliculas:
            eliminada = self.peliculas.pop(id)
            print(f"Película '{eliminada.titulo}' eliminada del catálogo.")
        else:
            print("Película no encontrada.")


# Crear catálogo
catalogo = CatalogoCine("Cine Estrella")

# Crear películas
p1 = Pelicula(1, "Interestelar", "Christopher Nolan", "Ciencia ficción", 169)
p2 = Pelicula(2, "Parasite", "Bong Joon-ho", "Drama", 132)
p3 = Pelicula(3, "Toy Story", "John Lasseter", "Animación", 81)

# Agregar al catálogo
catalogo.agregar_pelicula(p1)
catalogo.agregar_pelicula(p2)
catalogo.agregar_pelicula(p3)

# Listar todas las películas
catalogo.listar_peliculas()

# Editar una película
catalogo.editar_pelicula(3, genero="Animación / Aventura", duracion=85)

# Buscar una película
pelicula = catalogo.buscar_pelicula(2)
if pelicula:
    print("\nPelícula encontrada:")
    print(pelicula)

# Eliminar una película
catalogo.eliminar_pelicula(1)

# Listar de nuevo
catalogo.listar_peliculas()            