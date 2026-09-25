# ============================================================
# Tarea Práctica: Colecciones de datos en Python
# Sistema de Gestión de Registro de Contactos Telefónicos
# ============================================================

def mostrar_menu():
    print("\n--- GESTIÓN DE CONTACTOS TELEFÓNICOS ---")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto por nombre")
    print("4. Eliminar contacto")
    print("5. Salir")

def main():
    # Uso de Diccionario como colección principal (Clave: Nombre, Valor: Teléfono)
    contactos = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ").strip()
            if nombre in contactos:
                print(f"El contacto '{nombre}' ya existe con el número: {contactos[nombre]}")
            else:
                telefono = input("Ingrese el número de teléfono: ").strip()
                contactos[nombre] = telefono
                print(f"¡Contacto '{nombre}' agregado correctamente!")

        elif opcion == "2":
            if not contactos:
                print("La agenda de contactos está vacía.")
            else:
                print("\n--- LISTA DE CONTACTOS ---")
                for nombre, telefono in contactos.items():
                    print(f"• Nombre: {nombre} | Teléfono: {telefono}")

        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ").strip()
            if nombre in contactos:
                print(f"Contacto encontrado -> Nombre: {nombre} | Teléfono: {contactos[nombre]}")
            else:
                print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print(f"¡Contacto '{nombre}' eliminado correctamente!")
            else:
                print(f"No se pudo eliminar. El contacto '{nombre}' no existe.")

        elif opcion == "5":
            print("¡Gracias por utilizar el sistema de gestión de contactos!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()