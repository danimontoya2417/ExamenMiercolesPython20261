import random

usuarios_servicio = []

def generar_usuarios_iniciales():
    global usuarios_servicio
    nombres_ejemplo = ["Juan", "Ana", "Luis", "Carla", "Pedro", "Sara", "Mario", "Laura", "David", "Elena"]

    for i in range(10):
        usuarios = {
            "id": i + 1,
            "nombre": nombres_ejemplo[i],
            "documento": str(10000000 + i),
            "estrato": random.randint(1, 6),
            "consumoEnergetico": [random.randint(10, 90) for _ in range(30)],  # 30 consumos
            "estado": "ACTIVO"
        }
        usuarios_servicio.append(usuarios)

def listar_usuarios():
    global usuarios_servicio
    print("\n--- LISTA DE USUARIOS DEL SERVICIO ---")
    for u in usuarios_servicio:
        promedio = sum(u["consumoEnergetico"]) // len(u["consumoEnergetico"])
        print(f"ID: {u['id']}, Nombre: {u['nombre']}, Estrato: {u['estrato']}, Consumo promedio: {promedio} KWH")
    print()

def promedio(consumos):
    return sum(consumos) // len(consumos) 

def ordenar_por_consumo():
    usuarios_servicio.sort(key=lambda u: promedio(u["consumoEnergetico"]))
    print("\nUsuarios ordenados por consumo promedio.\n")
    listar_usuarios()  #

def menu_usuarios_servicio():
    global usuarios_servicio
    while True:
        print(" GESTIÓN USUARIOS SERVICIO ")
        print("1. Listar usuarios")
        print("2. Ordenar por consumo")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_usuarios()
        elif opcion == "2":
            ordenar_por_consumo()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.\n")