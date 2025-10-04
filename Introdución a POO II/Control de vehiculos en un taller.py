class Vehiculo:
    def __init__(self, id, marca, modelo, año, propietario, problema_reportado):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.año = año  # int: año de fabricación
        self.propietario = propietario
        self.problema_reportado = problema_reportado

    def __str__(self):
        return (f"ID: {self.id} | Propietario: {self.propietario}\n"
                f"  Vehículo: {self.marca} {self.modelo} ({self.año})\n"
                f"  Problema: {self.problema_reportado}")
    
class TallerMecanico:
    def __init__(self, nombre="Taller Central"):
        self.nombre = nombre
        self.vehiculos = {}  # Diccionario: id → Vehiculo

    def registrar_vehiculo(self, vehiculo):
        if vehiculo.id in self.vehiculos:
            print(f"Error: Ya existe un vehículo con ID {vehiculo.id}.")
        else:
            self.vehiculos[vehiculo.id] = vehiculo
            print(f"Vehículo de {vehiculo.propietario} registrado en {self.nombre}.")

    def listar_vehiculos(self):
        if not self.vehiculos:
            print(f"No hay vehículos registrados en {self.nombre}.")
        else:
            print(f"\n--- Vehículos en {self.nombre} ---")
            for vehiculo in self.vehiculos.values():
                print(vehiculo)
                print("-" * 50)

    def buscar_vehiculo(self, id):
        return self.vehiculos.get(id, None)

    def actualizar_vehiculo(self, id, marca=None, modelo=None, año=None,
                           propietario=None, problema_reportado=None):
        if id not in self.vehiculos:
            print("Vehículo no encontrado.")
            return

        vehiculo = self.vehiculos[id]
        if marca is not None:
            vehiculo.marca = marca
        if modelo is not None:
            vehiculo.modelo = modelo
        if año is not None:
            if 1886 <= año <= 2030:  # Rango razonable
                vehiculo.año = año
            else:
                print("Año inválido. Debe estar entre 1886 y 2030.")
                return
        if propietario is not None:
            vehiculo.propietario = propietario
        if problema_reportado is not None:
            vehiculo.problema_reportado = problema_reportado

        print(f"Vehículo ID {id} actualizado.")

    def eliminar_vehiculo(self, id):
        if id in self.vehiculos:
            eliminado = self.vehiculos.pop(id)
            print(f"Vehículo de {eliminado.propietario} eliminado del taller.")
        else:
            print("Vehículo no encontrado.")

# Crear taller
taller = TallerMecanico("Taller Veloz")

# Crear vehículos
v1 = Vehiculo(1, "Toyota", "Corolla", 2018, "Ana Martínez", "Fuga de aceite")
v2 = Vehiculo(2, "Honda", "Civic", 2020, "Luis Pérez", "Problema en el sistema de frenos")

# Registrar vehículos
taller.registrar_vehiculo(v1)
taller.registrar_vehiculo(v2)

# Listar vehículos
taller.listar_vehiculos()

# Actualizar un vehículo
taller.actualizar_vehiculo(1, problema_reportado="Fuga de aceite + cambio de filtro")

# Buscar un vehículo
vehiculo = taller.buscar_vehiculo(2)
if vehiculo:
    print("\nVehículo encontrado:")
    print(vehiculo)

# Eliminar un vehículo
taller.eliminar_vehiculo(1)

# Listar de nuevo
taller.listar_vehiculos()                