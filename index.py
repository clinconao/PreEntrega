# Diccionario para almacenar los usuarios y sus contraseñas
usuarios = {}

# Función para registrar un usuario
def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    usuario = input("Ingrese nombre de usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe. Intente con otro nombre de usuario.")
        return
    contraseña = input("Ingrese una contraseña: ")
    usuarios[usuario] = contraseña
    print(f"Usuario '{usuario}' registrado exitosamente.")

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    print("\n--- Usuarios Registrados ---")
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"Usuario: {usuario}")

# Función para el inicio de sesión
def login():
    print("\n--- Inicio de Sesión ---")
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario in usuarios:
        contraseña = input("Ingrese su contraseña: ")
        if usuarios[usuario] == contraseña:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Usuario")
        print("2. Mostrar Usuarios")
        print("3. Iniciar Sesión")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()