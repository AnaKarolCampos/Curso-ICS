''' Adicione um novo atributo endereco à classe Pessoa.
Modifique o método construtor para aceitar o novo atributo.
Crie um método que retorne o endereço completo da pessoa. '''

class Pessoa:
    nome = "Ana"
    sobrenome = "Campos"
    idade = 16
    profissao = "Estudante"
    endereco = None

    def __init__(self, endereco_passado):
        self.endereco = endereco_passado

    def modifica_endereco (self):
        return print(f"{self.nome} {self.sobrenome}, {self.idade} anos, {self.profissao}, {self.endereco}")

pessoa = Pessoa("rua tal, n° 1, bairro tal")
print(pessoa.modifica_endereco())