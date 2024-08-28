''' Crie um método aniversario que incremente a idade da pessoa em 1.
Teste o método instanciando um objeto e chamando o método aniversario '''

class Pessoa:
    nome = "Ana"
    sobrenome = "Campos"
    idade = 16
    profissao = "Estudante"
    endereco = "rua tal, n° 1, bairro tal"

    def aniversario (self):
        self.idade += 1
        return self.idade

pessoa = Pessoa()
print(pessoa.aniversario())