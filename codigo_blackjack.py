class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.oculta: bool = False


class Baraja:
    def __init__(self):
        self.cartas: list[Carta] = []

    def revolver(self):
        pass

    def repartir_carta(self, tapada: bool) -> Carta:
        pass

class Mano:
    def __init__(self, cartas):
        self.cartas: list[Carta] = []

    def es_blackjack(self) -> bool:
        pass

    def agregar_carta(self, carta) -> Carta:
        pass

    def calcular_mano(self):
        pass


class Blackjack:
    def registrar_jugador(self, nombre: str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass

    def turno_jugador(self):
        pass

    def turno_casa(self):
        pass

    def comparar_mano(self):
        pass

    def determinar_ganador(self):
        pass

    def finalizar_jugador(self):
        pass

class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas

    def inicializar_mano(self, cartas):
        pass

    def seleccionar_jugada(self):
        pass

    def fichas_finales_jugador(self):
        pass

class Casa:
    def __init__(self):
        self.mano = Mano()

    def mostrar_carta(self):
        pass
