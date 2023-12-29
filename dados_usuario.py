class DadosUsuario:
    def __init__(self, nome='', pontuacao=0):
        self.__nome = nome
        self.__pontuacao = pontuacao

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if self.__nome_eh_valido(novo_nome):
            self.__nome = novo_nome
        else:
            raise ValueError('O nome não é válido')

    @property
    def pontuacao(self) -> int:
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, nova_pontuacao: int):
        self.__pontuacao = nova_pontuacao

    @staticmethod
    def __nome_eh_valido(nome: str) -> bool:
        return len(nome) > 1 and nome.replace(' ', '').isalpha()
