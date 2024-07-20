''' Crie uma lista contendo vários objetos Pessoa.
Imprima os dados completos de cada pessoa na lista. '''

class Pessoa:
    nome = " "
    sobrenome = " "
    idade = None
    profissao = "estudante"

    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada, endereco_passado):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada
        self.endereco = endereco_passado

    def imprime_dados_completos(self):
        return print(f"{self.nome} {self.sobrenome}, {self.idade}, {self.profissao}, {self.endereco}")

pessoa = Pessoa("Ana", "Campos", 16, "Estudante", "rua tal, n° 1, bairro tal")
print(pessoa.imprime_dados_completos())

pessoa2 = Pessoa("Joanna", "Silva", 10, "Estudante", "rua tal, n° 1, bairro tal")
print(pessoa2.imprime_dados_completos())

pessoa3 = Pessoa("Carla", "Bernardina", 33, "Gerente", "rua tal, n° 1, bairro tal")
print(pessoa2.imprime_dados_completos())

pessoa4 = Pessoa("Junio", "Damasceno", 37, "Eletricista", "rua tal, n° 1, bairro tal")
print(pessoa2.imprime_dados_completos())