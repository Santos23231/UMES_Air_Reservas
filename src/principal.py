from autenticacion.autenticacion import login
from utilidades.menus import mostrar_menu_principal, mostrar_menu_admin, mostrar_menu_usuario, mostrar_menu_admin_completo


def main():
    usuario = login()

    if usuario:
        while True:
            if usuario["rol"] == "administrador":
                mostrar_menu_admin_completo(usuario)
                break
            elif usuario["rol"] == "pasajero":
                mostrar_menu_usuario(usuario)
                break
            else:
                print("\n¿Qué menú deseas ver?")
                print("1. Menú principal")
                print("2. Menú usuario")
                print("3. Salir")
                opcion = input("Selecciona una opción: ")
                if opcion == "1":
                    mostrar_menu_principal(usuario)
                elif opcion == "2":
                    mostrar_menu_usuario(usuario)
                elif opcion == "3":
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()