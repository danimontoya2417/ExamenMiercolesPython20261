usuarios = []

def registrar_usuario():
    print("\n--- REGISTRO ---")
    correo = input("Ingresa correo: ")
    contraseña = input("Ingresa una contraseña: ")

    # Verificar si el correo ya existe
    for u in usuarios:
        if u["correo"] == correo:
            print("El correo ya existe en la bd\n")
            return

    # Crear un nuevo usuario
    nuevo_usuario = {
        "correo": correo,
        "contraseña": contraseña
    }

    usuarios.append(nuevo_usuario)
    print("Usuario registrado\n")


def login():
    print("\n INICIO DE SESIÓN ")
    intentos = 3

    while intentos > 0:
        correo_ing = input("Correo: ")
        contraseña_ing = input("Contraseña: ")

        encontrado = False

        # Buscar usuario
        for u in usuarios:
            if u["correo"] == correo_ing and u["contraseña"] == contraseña_ing:
                print("Bienvenido\n")
                encontrado = True
                break

        if encontrado:
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

    print("Cuenta bloqueada temporalmente.\n")
    return False
