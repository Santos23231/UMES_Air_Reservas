from autenticacion.autenticacion import login
from utilidades.menus import mostrar_menu_principal, mostrar_menu_admin, mostrar_menu_usuario


def main():
    usuario = login()

    if usuario:
        while True:
            print("\n¿Qué menú deseas ver?")
            print("1. Menú principal")
            print("2. Menú administrador")
            print("3. Menú usuario")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                mostrar_menu_principal(usuario)
            elif opcion == "2":
                mostrar_menu_admin()
            elif opcion == "3":
                mostrar_menu_usuario()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()