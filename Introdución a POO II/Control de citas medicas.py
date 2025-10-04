from datetime import datetime, time

class CitaMedica:
    def __init__(self, id, paciente, medico, fecha, hora, motivo):
        self.id = id
        self.paciente = paciente      # str: nombre del paciente
        self.medico = medico          # str: nombre del médico
        self.fecha = fecha            # datetime.date
        self.hora = hora              # datetime.time
        self.motivo = motivo          # str: motivo de la consulta

    def __str__(self):
        fecha_str = self.fecha.strftime("%Y-%m-%d")
        hora_str = self.hora.strftime("%H:%M")
        return (f"ID: {self.id} | Paciente: {self.paciente} | Médico: {self.medico}\n"
                f"  Fecha: {fecha_str} | Hora: {hora_str} | Motivo: {self.motivo}")
    
class GestorCitas:
    def __init__(self):
        self.citas = {}  # Diccionario: id → CitaMedica

    def agendar_cita(self, cita):
        if cita.id in self.citas:
            print(f"Error: Ya existe una cita con ID {cita.id}.")
            return False

        # Opcional: verificar que no haya conflicto de horario para el mismo médico
        for c in self.citas.values():
            if (c.medico == cita.medico and
                c.fecha == cita.fecha and
                c.hora == cita.hora):
                print(f"Error: El médico {cita.medico} ya tiene una cita a esa fecha y hora.")
                return False

        self.citas[cita.id] = cita
        print(f"Cita agendada para {cita.paciente} con {cita.medico}.")
        return True

    def listar_citas(self):
        if not self.citas:
            print("No hay citas registradas.")
        else:
            print("\n--- Lista de Citas Médicas ---")
            for cita in self.citas.values():
                print(cita)
                print("-" * 50)

    def buscar_cita(self, id):
        return self.citas.get(id, None)

    def actualizar_cita(self, id, paciente=None, medico=None, fecha=None, hora=None, motivo=None):
        if id not in self.citas:
            print("Cita no encontrada.")
            return False

        cita = self.citas[id]

        # Guardar valores originales por si hay conflicto
        medico_orig = cita.medico
        fecha_orig = cita.fecha
        hora_orig = cita.hora

        # Aplicar cambios
        if paciente is not None:
            cita.paciente = paciente
        if medico is not None:
            cita.medico = medico
        if fecha is not None:
            cita.fecha = fecha
        if hora is not None:
            cita.hora = hora
        if motivo is not None:
            cita.motivo = motivo

        # Verificar conflicto de horario (solo si cambió médico, fecha o hora)
        if (cita.medico != medico_orig or cita.fecha != fecha_orig or cita.hora != hora_orig):
            for cid, c in self.citas.items():
                if cid != id and c.medico == cita.medico and c.fecha == cita.fecha and c.hora == cita.hora:
                    # Revertir cambios
                    cita.paciente = self.citas[id].paciente  # no necesario si no se cambió
                    cita.medico = medico_orig
                    cita.fecha = fecha_orig
                    cita.hora = hora_orig
                    cita.motivo = self.citas[id].motivo
                    print("Error: Conflicto de horario. El médico ya tiene una cita a esa fecha y hora.")
                    return False

        print(f"Cita ID {id} actualizada.")
        return True

    def cancelar_cita(self, id):
        if id in self.citas:
            cancelada = self.citas.pop(id)
            print(f"Cita de {cancelada.paciente} con {cancelada.medico} cancelada.")
        else:
            print("Cita no encontrada.")    


from datetime import date, time

# Crear gestor
gestor = GestorCitas()

# Crear citas
cita1 = CitaMedica(
    id=1,
    paciente="Ana Martínez",
    medico="Dr. López",
    fecha=date(2025, 4, 15),
    hora=time(10, 30),
    motivo="Dolor de cabeza persistente"
)

cita2 = CitaMedica(
    id=2,
    paciente="Carlos Ruiz",
    medico="Dra. Gómez",
    fecha=date(2025, 4, 15),
    hora=time(11, 0),
    motivo="Chequeo anual"
)

# Agendar citas
gestor.agendar_cita(cita1)
gestor.agendar_cita(cita2)

# Intentar agendar cita duplicada en horario
cita3 = CitaMedica(
    id=3,
    paciente="Luis Pérez",
    medico="Dr. López",
    fecha=date(2025, 4, 15),
    hora=time(10, 30),  # Mismo horario que cita1
    motivo="Fiebre"
)
gestor.agendar_cita(cita3)  # ← Mostrará error de conflicto

# Listar citas
gestor.listar_citas()

# Actualizar una cita
gestor.actualizar_cita(1, motivo="Migraña crónica", hora=time(14, 0))

# Cancelar una cita
gestor.cancelar_cita(2)

# Listar de nuevo
gestor.listar_citas()             