class Pessoa:
    def __init__(self, nome, taxa, renda):
        self.taxaImposto = taxa
        self.rendaAnual = renda
        self.nome = nome

    def calcularImpostoRenda(self):
        pass

class PessoaFisica(Pessoa):
    def calcularImpostoRenda(self):
        print(f'{self.nome}, valor a pagar de IR: {self.rendaAnual*self.taxaImposto}')

class PessoaJuridica(Pessoa):
    def calcularImpostoRenda(self):
        print(f'{self.nome}, valor a pagar de IR: {self.rendaAnual * self.taxaImposto}')

from enum import Enum

class PessoaType(Enum):
    JURIDICA = 1
    FISICA = 2

class PessoaFactory:
    @staticmethod
    def create(Pessoa_type: PessoaType) -> Pessoa:
        if Pessoa_type == PessoaType.FISICA:
            return PessoaFisica('João da Silva', 0.25, 12000)
        if Pessoa_type == PessoaType.JURIDICA:
            return PessoaJuridica('Quitanda Pôr do Sol', 0.15, 45000)

        return None

if __name__ == '__main__':
    pJuridica = PessoaFactory.create(PessoaType.JURIDICA)
    pFisica = PessoaFactory.create(PessoaType.FISICA)

    pFisica.calcularImpostoRenda()
    pJuridica.calcularImpostoRenda()
