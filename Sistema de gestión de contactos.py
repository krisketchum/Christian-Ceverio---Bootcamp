# Clase que representa un contacto
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion


# Clase agenda
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, nombre, telefono, correo, direccion):
        self.contactos.append(Contacto(nombre, telefono, correo, direccion))

    # Buscar por nombre o teléfono
    def buscar(self, valor):
        valor = valor.lower()
        encontrado = False

        for c in self.contactos:
            if valor in c.nombre.lower() or valor in c.telefono.lower():
                print("------------------------")
                print(f"Nombre    : {c.nombre}")
                print(f"Teléfono  : {c.telefono}")
                print(f"Correo    : {c.correo}")
                print(f"Dirección : {c.direccion}")
                encontrado = True

        if not encontrado:
            print("No se ha encontrado ningún contacto con esos datos.")

    # Editar un contacto buscándolo por cualquier dato
    def editar(self, valor, nombre="", telefono="", correo="", direccion=""):
        valor = valor.lower()

        for c in self.contactos:
            datos = f"{c.nombre} {c.telefono} {c.correo} {c.direccion}".lower()
            if valor in datos:
                if nombre:
                    c.nombre = nombre
                if telefono:
                    c.telefono = telefono
                if correo:
                    c.correo = correo
                if direccion:
                    c.direccion = direccion
                print("Contacto actualizado")
                return

        print("No se ha encontrado ningún contacto con esos datos.")

    def eliminar(self, telefono):
        self.contactos = [c for c in self.contactos if c.telefono != telefono]


agenda = Agenda()

# Menú principal
while True:
    print("\n1. Agregar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Eliminar")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agenda.agregar(
            input("Nombre: "),
            input("Teléfono: "),
            input("Correo: "),
            input("Dirección: ")
        )
        print("Contacto agregado")

    elif opcion == "2":
        agenda.buscar(input("Buscar (nombre o teléfono): "))

    elif opcion == "3":
        agenda.editar(
            input("Dato para buscar contacto: "),
            input("Nuevo nombre: "),
            input("Nuevo teléfono: "),
            input("Nuevo correo: "),
            input("Nueva dirección: ")
        )

    elif opcion == "4":
        agenda.eliminar(input("Teléfono: "))
        print("Contacto eliminado")

    elif opcion == "5":
        print("Saliendo del programa.")
        break
