'''
Crie métodos modificar_nome e modificar_sobrenome para alterar o nome e o sobrenome da pessoa.
Teste os métodos instanciando um objeto e modificando seus dados.
'''

class Pessoa:
    nome = " "
    sobrenome = " "
    idade = None

    def __init__(self, nome_passado, sobrenome_passado, idade_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada

    def imprime_dados_completos(self):
        return print(f"{self.nome} {self.sobrenome}, {self.idade} anos.")

    def modificar_nome(self, novo_nome):
        self.nome = novo_nome

    def modificar_sobrenome(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

pessoa1 = Pessoa("Ana", "Karolyne", 16)

pessoa1.imprime_dados_completos()

pessoa1.modificar_nome("Ana")
pessoa1.modificar_sobrenome("Campos")

pessoa1.imprime_dados_completos()