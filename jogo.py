from jogador import JogadorHumano, JogadorAleatorioComputador
import time
import math 


class JogoDaVelha:
    global jogar
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]
        self.vencedor_atual = None 
    def printar_tabuleiro(self):
        for risco in [self.tabuleiro[i*3:(i+1)*3] for i in range(3)]:
            print('I ' + ' I '.join(risco) + ' I')

    @staticmethod
    def num_tabuleiro():
        numero_tabuleiro = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for num in numero_tabuleiro:
            print('I ' + ' I '.join(num) + ' I')

    def jogadas_realizadas(self):
        return [i for i, x in enumerate(self.tabuleiro) if x == ' ']
    
    def quadrado_vazio(self):
        return ' ' in self.tabuleiro
    
    def num_quadrados_vazios(self):
        return self.tabuleiro.count(' ')
    
    def vencedor(self, quadrado, letra):
        risco_ind = quadrado//3
        risco = self.tabuleiro[risco_ind*3: (risco_ind + 1) * 3]
        if all([x == letra for x in risco]):
            return True
        col_ind = quadrado % 3 
        coluna = [self.tabuleiro[col_ind+i*3]for i in range(3)]
        if all([x == letra for x in coluna]):
            return True
        
        if quadrado % 2 == 0:
            diagonal_1 = [self.tabuleiro[i] for i in [0, 4, 8]]
            if all([x == letra for x in diagonal_1]):
               return True
        
            diagonal_2 = [self.tabuleiro[i] for i in [2, 4, 6]]
            if all([x == letra for x in diagonal_2]):
               return True
            
        return False
    
    def realizar_jogada(self, quadrado, letra):
        if self.tabuleiro[quadrado] == ' ':
            self.tabuleiro[quadrado] = letra
            if self.vencedor(quadrado, letra):
                self.vencedor_atual = letra
            return True
        return False

    def jogar(jogo, jogador_x, jogador_o, printar_jogo = True):
        if printar_jogo:
            jogo.printar_tabuleiro
        letra = 'X'

        while jogo.num_quadrados_vazios():
            if letra == 'O':
                quadrado = jogador_o.jogada(jogo)
            else:
                quadrado = jogador_x.jogada(jogo)
            if jogo.realizar_jogada(quadrado, letra):
                if printar_jogo:
                    print(letra + f', realize uma jogada no quadrado {quadrado}')
                    jogo.printar_tabuleiro()
                    print('')

                if jogo.vencedor_atual:
                    if printar_jogo:
                        print(letra + ' VENCEU!')
                    return letra
                
                letra = 'O' if letra == 'X' else 'X'
            time.sleep(2)

        if printar_jogo:
            print('Empate!')

if __name__=='__main__':
   jogador_x = JogadorHumano('X')
   jogador_o = JogadorAleatorioComputador('O')
   jv = JogoDaVelha()
   jogar(jv, jogador_x, jogador_o, printar_jogo = True)