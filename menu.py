def datos_daniel():
    print("Mi nommbre es Daniel Aedo y tengo 29 años")

def datos_patricio():
    print("Mi nombre es Patricio Céspedes y tengo 30 años.")

# Menú base del programa
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        datos_daniel()
    elif op == "2":
        datos_patricio()
    elif op == "3":
        pass # Aquí se llamará a la función del integrante 3
    else:
        print(" Opción inválida.")
