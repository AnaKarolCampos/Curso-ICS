''' Crie um método modifica_profissao na classe Pessoa que permita modificar a profissão da pessoa.
Teste o método alterando a profissão de um objeto instanciado.
'''

class Pessoa:
    nome = "Ana"
    sobrenome = "Campos"
    idade = 16
    profissao = " "

    def __init__(self, profissao_passada):
        self.profissao = profissao_passada

    def modifica_profissao (self):
        return print(f"{self.nome} {self.sobrenome}, {self.idade} anos, {self.profissao}")

pessoa = Pessoa("Estudante")
print(pessoa.modifica_profissao())