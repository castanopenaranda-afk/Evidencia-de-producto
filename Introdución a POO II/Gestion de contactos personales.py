class Contacto:
    def __init__(self, id, nombre, telefono, email, direccion):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | Teléfono: {self.telefono} | "
                f"Email: {self.email} | Dirección: {self.direccion}")
    

class Agenda:
    def __init__(self):
        self.contactos = {}  # Diccionario: id → Contacto (acceso rápido)

    def agregar_contacto(self, contacto):
        if contacto.id in self.contactos:
            print(f"Error: Ya existe un contacto con ID {contacto.id}.")
        else:
            self.contactos[contacto.id] = contacto
            print(f"Contacto '{contacto.nombre}' agregado correctamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("\n--- Lista de Contactos ---")
            for contacto in self.contactos.values():
                print(contacto)

    def buscar_contacto(self, id):
        return self.contactos.get(id, None)

    def editar_contacto(self, id, nombre=None, telefono=None, email=None, direccion=None):
        if id not in self.contactos:
            print("Contacto no encontrado.")
            return

        contacto = self.contactos[id]
        if nombre is not None:
            contacto.nombre = nombre
        if telefono is not None:
            contacto.telefono = telefono
        if email is not None:
            contacto.email = email
        if direccion is not None:
            contacto.direccion = direccion

        print(f"Contacto ID {id} actualizado.")

    def eliminar_contacto(self, id):
        if id in self.contactos:
            eliminado = self.contactos.pop(id)
            print(f"Contacto '{eliminado.nombre}' eliminado.")
        else:
            print("Contacto no encontrado.")    

 # Crear la agenda
agenda = Agenda()

# Crear contactos
c1 = Contacto(1, "Ana López", "555-1234", "ana@example.com", "Calle Falsa 123")
c2 = Contacto(2, "Carlos Ruiz", "555-5678", "carlos@example.com", "Av. Siempre Viva 456")

# Agregar contactos
agenda.agregar_contacto(c1)
agenda.agregar_contacto(c2)

# Listar todos
agenda.listar_contactos()

# Editar un contacto
agenda.editar_contacto(1, telefono="555-9999", email="ana.nueva@example.com")

# Buscar un contacto
contacto = agenda.buscar_contacto(2)
if contacto:
    print("\nContacto encontrado:", contacto)

# Eliminar un contacto
agenda.eliminar_contacto(2)

# Listar de nuevo
agenda.listar_contactos()           