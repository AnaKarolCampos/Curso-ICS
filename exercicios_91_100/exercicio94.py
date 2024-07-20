''' Crie um método comparar_idade que compare a idade de duas pessoas e retorne quem é mais velho. '''

class Pessoa:
    nome = " "
    sobrenome = " "
    idade = None
    profissao = " "
    endereco = " "

    def aniversario (self):
        self.idade += 1
        return self.idade
    
    def __init__(self, nome_passado, sobrenome_passado, idade_passada, profissao_passada, endereco_passado):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        self.profissao = profissao_passada
        self.endereco = endereco_passado
    
    def comparar_idade (self, pessoa1, pessoa2):
        if pessoa1.idade > pessoa2.idade:
            return f"{pessoa1.nome} é mais velho(a) que {pessoa2.nome}"
        elif pessoa1.idade < pessoa2.idade:
            return f"{pessoa2.nome} é mais velho(a) que {pessoa1.nome}"
        else:
            return f"{pessoa1.nome} e {pessoa2.nome} têm a mesma idade"

pessoa1 = Pessoa("Ana", "Campos", 16, "Estudante", "rua tal, n° 1, bairro tal")
pessoa2 = Pessoa("Fulana", "Silva", 18, "Vendedora", "rua tal, n° 15, bairro tal")

resultado = Pessoa.comparar_idade(pessoa1, pessoa2)
print(resultado)