class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | Descripción: {self.descripcion} | "
                f"Precio: ${self.precio:.2f} | Cantidad: {self.cantidad}")
    
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: id → Producto (acceso rápido)

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print(f"Error: Ya existe un producto con ID {producto.id}.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto '{producto.nombre}' agregado correctamente.")

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario ---")
            for producto in self.productos.values():
                print(producto)

    def buscar_producto(self, id):
        return self.productos.get(id, None)

    def actualizar_producto(self, id, nombre=None, descripcion=None, precio=None, cantidad=None):
        if id not in self.productos:
            print("Producto no encontrado.")
            return

        producto = self.productos[id]
        if nombre is not None:
            producto.nombre = nombre
        if descripcion is not None:
            producto.descripcion = descripcion
        if precio is not None:
            if precio >= 0:
                producto.precio = precio
            else:
                print("El precio no puede ser negativo.")
                return
        if cantidad is not None:
            if cantidad >= 0:
                producto.cantidad = cantidad
            else:
                print("La cantidad no puede ser negativa.")
                return
        print(f"Producto ID {id} actualizado.")

    def eliminar_producto(self, id):
        if id in self.productos:
            eliminado = self.productos.pop(id)
            print(f"Producto '{eliminado.nombre}' eliminado.")
        else:
            print("Producto no encontrado.")



# Crear inventario
inventario = Inventario()

# Crear productos
p1 = Producto(1, "Laptop", "Laptop gamer de 16GB RAM", 1200.0, 10)
p2 = Producto(2, "Mouse", "Mouse inalámbrico", 25.5, 50)

# Agregar al inventario
inventario.agregar_producto(p1)
inventario.agregar_producto(p2)

# Listar
inventario.listar_productos()

# Actualizar
inventario.actualizar_producto(1, precio=1150.0, cantidad=8)

# Buscar
prod = inventario.buscar_producto(2)
if prod:
    print("\nProducto encontrado:", prod)

# Eliminar
inventario.eliminar_producto(2)

# Listar de nuevo
inventario.listar_productos()