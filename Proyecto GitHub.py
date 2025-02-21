import random

equipos = ["Barcelona", "Real Madrid", "Manchester United", "Bayern Munich", "Juventus", "PSG", "Liverpool", "Chelsea"]
historial = []

def simular_partido():
    e1, e2 = random.sample(equipos, 2)
    g1, g2 = random.randint(0, 7), random.randint(0, 7)
    resultado = f"{e1} {g1} - {g2} {e2}"
    historial.append(resultado)
    print(resultado)


