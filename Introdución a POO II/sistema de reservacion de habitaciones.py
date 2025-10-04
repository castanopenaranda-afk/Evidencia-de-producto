from datetime import date, timedelta

class Reserva:
    def __init__(self, id, nombre_cliente, numero_habitacion, fecha_reserva, duracion_estadia):
        self.id = id
        self.nombre_cliente = nombre_cliente
        self.numero_habitacion = numero_habitacion
        self.fecha_reserva = fecha_reserva          # date: inicio de la estancia
        self.duracion_estadia = duracion_estadia    # int: número de noches

    def fecha_salida(self):
        return self.fecha_reserva + timedelta(days=self.duracion_estadia)

    def __str__(self):
        salida = self.fecha_salida()
        return (f"ID: {self.id} | Cliente: {self.nombre_cliente} | Habitación: {self.numero_habitacion}\n"
                f"  Check-in: {self.fecha_reserva} | Check-out: {salida} | Noches: {self.duracion_estadia}")
    


class SistemaReservas:
    def __init__(self):
        self.reservas = {}  # Diccionario: id → Reserva

    def _habitacion_disponible(self, numero_habitacion, fecha_inicio, duracion):
        """Verifica si la habitación está disponible en el rango de fechas."""
        fecha_fin = fecha_inicio + timedelta(days=duracion)
        for reserva in self.reservas.values():
            if reserva.numero_habitacion == numero_habitacion:
                salida_reserva = reserva.fecha_salida()
                # Solapamiento: si las fechas se cruzan
                if fecha_inicio < salida_reserva and fecha_fin > reserva.fecha_reserva:
                    return False
        return True

    def crear_reserva(self, reserva):
        if reserva.id in self.reservas:
            print(f"Error: Ya existe una reserva con ID {reserva.id}.")
            return False

        if not self._habitacion_disponible(
            reserva.numero_habitacion,
            reserva.fecha_reserva,
            reserva.duracion_estadia
        ):
            print(f"Error: La habitación {reserva.numero_habitacion} no está disponible "
                  f"del {reserva.fecha_reserva} al {reserva.fecha_salida()}.")
            return False

        self.reservas[reserva.id] = reserva
        print(f"Reserva creada para {reserva.nombre_cliente} en habitación {reserva.numero_habitacion}.")
        return True

    def listar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
        else:
            print("\n--- Lista de Reservas ---")
        for reserva in self.reservas.values():
                print(reserva)
                print("-" * 50)

    def buscar_reserva(self, id):
        return self.reservas.get(id, None)

    def actualizar_reserva(self, id, nombre_cliente=None, numero_habitacion=None,
                          fecha_reserva=None, duracion_estadia=None):
        if id not in self.reservas:
            print("Reserva no encontrada.")
            return False

        reserva_original = self.reservas[id]

        # Guardar valores actuales por si hay conflicto
        hab_orig = reserva_original.numero_habitacion
        fecha_orig = reserva_original.fecha_reserva
        duracion_orig = reserva_original.duracion_estadia

        # Aplicar cambios temporales
        if nombre_cliente is not None:
            reserva_original.nombre_cliente = nombre_cliente
        if numero_habitacion is not None:
            reserva_original.numero_habitacion = numero_habitacion
        if fecha_reserva is not None:
            reserva_original.fecha_reserva = fecha_reserva
        if duracion_estadia is not None:
            reserva_original.duracion_estadia = duracion_estadia

        # Verificar disponibilidad con los nuevos datos
        if not self._habitacion_disponible(
            reserva_original.numero_habitacion,
            reserva_original.fecha_reserva,
            reserva_original.duracion_estadia
        ):
            # Revertir cambios
            reserva_original.numero_habitacion = hab_orig
            reserva_original.fecha_reserva = fecha_orig
            reserva_original.duracion_estadia = duracion_orig
            print("Error: La habitación no está disponible en las nuevas fechas.")
            return False

        print(f"Reserva ID {id} actualizada.")
        return True

    def eliminar_reserva(self, id):
        if id in self.reservas:
            eliminada = self.reservas.pop(id)
            print(f"Reserva de {eliminada.nombre_cliente} en habitación {eliminada.numero_habitacion} eliminada.")
        else:
            print("Reserva no encontrada.")


from datetime import date

# Crear sistema
sistema = SistemaReservas()

# Crear reservas
r1 = Reserva(
    id=1,
    nombre_cliente="María López",
    numero_habitacion=101,
    fecha_reserva=date(2025, 6, 10),
    duracion_estadia=3  # 3 noches → check-out: 13 de junio
)

r2 = Reserva(
    id=2,
    nombre_cliente="Carlos Ruiz",
    numero_habitacion=102,
    fecha_reserva=date(2025, 6, 12),
    duracion_estadia=2
)

# Crear reservas
sistema.crear_reserva(r1)
sistema.crear_reserva(r2)

# Intentar reservar la misma habitación en fechas solapadas
r3 = Reserva(
    id=3,
    nombre_cliente="Ana Gómez",
    numero_habitacion=101,
    fecha_reserva=date(2025, 6, 12),  # Solapa con r1 (10–13)
    duracion_estadia=2
)
sistema.crear_reserva(r3)  # ← Mostrará error

# Listar reservas
sistema.listar_reservas()

# Actualizar una reserva
sistema.actualizar_reserva(2, duracion_estadia=4)  # Extender estancia

# Eliminar una reserva
sistema.eliminar_reserva(1)

# Listar de nuevosistema.listar_reservas()

# Actualizar una reserva
sistema.actualizar_reserva(2, duracion_estadia=4)  # Extender estancia

# Eliminar una reserva
sistema.eliminar_reserva(1)

# Listar de nuevo
sistema.listar_reservas()
sistema.listar_reservas()            