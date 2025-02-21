import random

equipos = ["Barcelona", "Real Madrid", "Manchester United", "Bayern Munich", "Juventus", "PSG", "Liverpool", "Chelsea"]
historial = []

def simular_partido():
    e1, e2 = random.sample(equipos, 2)
    g1, g2 = random.randint(0, 7), random.randint(0, 7)
    resultado = f"{e1} {g1} - {g2} {e2}"
    historial.append(resultado)
    print(resultado)

def ver_historial():
    print("\n".join(historial) if historial else "No hay partidos en el historial.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Simular partido")
        print("2. Ver historial")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            simular_partido()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()