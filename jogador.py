import math
import random

class Jogador:
    def __init__(self, letra):
        self.letra = letra 

    def jogada(self, jogo):
        pass 

class JogadorAleatorioComputador(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def jogada(self, jogo):
        quadrado = random.choice(jogo.jogadas_realizadas())
        return quadrado

class JogadorHumano(Jogador):
    def __init__(self, letra):
        super().__init__(letra)

    def jogada(self, jogo):
        quadrado_valido = False
        valor = None
        while not quadrado_valido:
            quadrado = input(self.letra + ', sua vez. Escolha um numero (0-8):')
            try:
                valor = int(quadrado)
                if valor not in jogo.jogadas_realizadas():
                    raise ValueError
                quadrado_valido = True
            except ValueError:
                print('Quadrado invalido. Tente novamente.')

        return valor