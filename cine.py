def mostrar_funciones():
    print("\nFunciones disponibles:")
    for i, funcion in enumerate(funciones):
        print(f"{i + 1}. {funcion['pelicula']} - {funcion['hora']}")

def hacer_reserva():
    nombre = input("\nNombre del cliente: ")
    mostrar_funciones()
    opcion = int(input("Seleccione el número de la función: ")) - 1

    if opcion < 0 or opcion >= len(funciones):
        print("Opción no válida.")
        return

    cantidad = int(input("Cantidad de boletos a comprar: "))
    total = cantidad * precio_boleto
    funcion = funciones[opcion]

    reserva = {
        "cliente": nombre,
        "pelicula": funcion["pelicula"],
        "hora": funcion["hora"],
        "boletos": cantidad,
        "total": total
    }
    reservas.append(reserva)

    print("\n--- Resumen de la Reserva ---")
    print(f"Cliente: {nombre}")
    print(f"Película: {funcion['pelicula']}")
    print(f"Hora: {funcion['hora']}")
    print(f"Boletos: {cantidad}")
    print(f"Total a pagar: Q{total:.2f}")

def mostrar_reservas():
    if not reservas:
        print("\nNo hay reservas registradas.")
    else:
        print("\n--- Todas las Reservas ---")
        for i, r in enumerate(reservas, 1):
            print(f"{i}. {r['cliente']} - {r['pelicula']} - {r['hora']} - {r['boletos']} boletos - Q{r['total']:.2f}")
def cancelar_reserva():
    nombre = input("\nIngrese el nombre del cliente para cancelar su reserva: ")
    global reservas
    antes = len(reservas)
    reservas = [r for r in reservas if r["cliente"] != nombre]
    despues = len(reservas)
    if antes == despues:
        print("No se encontró ninguna reserva con ese nombre.")
    else:
        print("Reserva(s) cancelada(s) exitosamente.")
precio_boleto = 35.00
funciones = [
    {"pelicula": "Avengers: Endgame", "hora": "15:00"},
    {"pelicula": "Toy Story 4", "hora": "17:30"},
    {"pelicula": "Joker", "hora": "20:00"}
]
reservas = []
while True:
    print("\n--- CineFácil ---")
    print("1. Hacer una reserva")
    print("2. Mostrar reservas")
    print("3. Cancelar reserva")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hacer_reserva()
    elif opcion == "2":
        mostrar_reservas()
    elif opcion == "3":
        cancelar_reserva()
    elif opcion == "4":
        print("Gracias por usar CineFácil.")
        break
    else:
        print("Opción inválida.")
