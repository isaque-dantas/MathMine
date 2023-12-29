from random import shuffle, randint, choice
from sympy import Eq, solve, symbols, core
from collections import namedtuple

EquationNumber = namedtuple('EquationNumber', ['coeficiente', 'tem_x'])


class GeradorEquacoes:
    def __init__(self, dificuldade=3):

        config_dificuldade = {
            1: [3, 1, (1, 5), '+'],
            2: [3, 1, (0, 10), '+'],
            3: [3, 1, (-3, 7), '+'],
            4: [3, 1, (-5, 10), '+'],
            5: [3, 2, (-5, 10), '+'],
            6: [4, 2, (-5, 10), '+'],
            7: [4, 2, (-10, 10), '+-'],
            8: [4, 3, (-10, 10), '+-'],
        }
        if dificuldade not in config_dificuldade:
            dificuldade = config_dificuldade[-1]
        self.__dificuldade = dificuldade

        (self.__qtd_termos,
         self.__qtd_x,
         self.__intervalo,
         self.__operacoes) = config_dificuldade[dificuldade]

        self.__operacoes = list(self.__operacoes)

    def __gerar_lista_vazia(self) -> list:
        return [None for i in range(self.__qtd_termos)]

    def __gerar_numeros_aleatorios(self) -> list:
        numeros_aleatorios = self.__gerar_lista_vazia()
        for i in range(len(numeros_aleatorios)):
            numero_aleatorio = randint(*self.__intervalo)
            numero_aleatorio = str(numero_aleatorio)
            numeros_aleatorios[i] = numero_aleatorio

        return numeros_aleatorios

    def __gerar_posicoes_elementos_equacao(self) -> list:
        posicoes_elementos_equacao = self.__gerar_lista_vazia()
        for i in range(self.__qtd_x):
            posicoes_elementos_equacao[i] = 'x'
        posicoes_elementos_equacao[self.__qtd_x] = '='

        shuffle(posicoes_elementos_equacao)

        while posicoes_elementos_equacao.index('=') in [0, self.__qtd_termos - 1]:
            shuffle(posicoes_elementos_equacao)

        return posicoes_elementos_equacao

    def __gerar_operacoes(self) -> list:
        operacoes = []
        for i in range(self.__qtd_termos):
            operacoes.append(choice(self.__operacoes))

        return operacoes

    def gerar_resposta_equacao(self, lista_equacao: list) -> float:
        x = symbols('x')

        funcoes_operacoes = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }

        membros_equacao = [self.__converter_equation_number(lista_equacao[0])]
        for operacao, numero_posterior in zip(lista_equacao[1:-1], lista_equacao[2:]):
            if operacao == '=':
                membros_equacao.append(self.__converter_equation_number(numero_posterior))
            elif operacao in ['+', '-', '*', '/']:
                numero_posterior = self.__converter_equation_number(numero_posterior)
                membros_equacao[-1] = funcoes_operacoes[operacao](membros_equacao[-1], numero_posterior)
        equacao = Eq(*membros_equacao)
        solucao = solve(equacao, x)
        if not solucao:
            solucao = None
        else:
            solucao = solucao[0]
        return solucao

    @staticmethod
    def __converter_equation_number(n: EquationNumber):
        if n.tem_x:
            return n.coeficiente * symbols('x')
        else:
            return n.coeficiente

    def gerar_lista_equacao(self):
        equacao = []
        posicoes_elementos_equacao = self.__gerar_posicoes_elementos_equacao()
        numeros_aleatorios = self.__gerar_numeros_aleatorios()
        operacoes = self.__gerar_operacoes()

        for i, (elemento, numero_aleatorio) in enumerate(zip(posicoes_elementos_equacao, numeros_aleatorios)):
            if elemento == '=':
                equacao.append(elemento)
            numero_equacao = EquationNumber(coeficiente=int(numero_aleatorio), tem_x=elemento == 'x')
            equacao.append(numero_equacao)

        posicoes_operacoes = []
        for i, (elemento, operacao) in enumerate(zip(equacao[1:], operacoes), 1):
            elemento_anterior = equacao[i - 1]

            if '=' in [elemento, elemento_anterior]:
                continue
            elif elemento == 0 and operacao == '/':
                operacao = '+'

            posicoes_operacoes.append((i, operacao))

        for i, (posicao, operacao) in enumerate(posicoes_operacoes):
            equacao.insert(posicao + i, operacao)

        return equacao

    def gerar_equacao(self):
        lista_equacao = self.gerar_lista_equacao()
        solucao = self.gerar_resposta_equacao(lista_equacao)
        equacao = self.gerar_str_equacao(lista_equacao)

        return equacao, solucao

    @staticmethod
    def gerar_str_equacao(lista_equacao):
        for i, elemento in enumerate(lista_equacao):
            if isinstance(elemento, EquationNumber):
                lista_equacao[i] = str(elemento.coeficiente) + 'x' if elemento.tem_x else str(elemento.coeficiente)
                if elemento.coeficiente < 0:
                    lista_equacao[i] = f'({lista_equacao[i]})'
        return ' '.join(lista_equacao)


def main():
    gerador = GeradorEquacoes(dificuldade=1)
    equacao, solucao = gerador.gerar_equacao()
    print(type(solucao))
    print(equacao, solucao, sep='; ')


if __name__ == '__main__':
    main()
