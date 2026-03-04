from modulos.Login import registrar_usuario, login
from modulos.Usuarios_Servicios import generar_usuarios_iniciales, menu_usuarios_servicio

def menu_principal():
    while True:
        print("menu principal")
        print("1. gestionar usuarios del servicio")
        print("2. salir")

        opcion = input("elija una opcion: ")


        if opcion == "1":
            menu_usuarios_servicio()
        elif opcion == "2":
            print ("saliendo \n")
            break
        else:
            print ("opcion invalida \n")

def menu_inicial():
    generar_usuarios_iniciales()
    while True:
        print ("sistema")
        print ("1. registrarse")
        print ("2. iniciar sesion")
        print ("3. salir")

        opcion = input("selecionar una opcion: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            if login():
                menu_principal()
            else:
                break
        elif opcion == "3":
            print("hasta luego. \n")
            break
        else:
            print("opcion no valida.\n")

menu_inicial()