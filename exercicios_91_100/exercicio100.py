'''
Adicione um método de classe criar_pessoa_anonima que cria uma pessoa com nome "Anonimo" e sobrenome "Silva".
Teste o método instanciando um objeto usando Pessoa.criar_pessoa_anonima.
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
        print(f"{self.nome} {self.sobrenome}, {self.idade} anos.")

    @classmethod
    def criar_pessoa_anonima(cls):
        return cls("Anonimo", "Silva", 0)  # não sabemos a idade do anônimo
    
pessoa_anonima = Pessoa.criar_pessoa_anonima()

pessoa_anonima.imprime_dados_completos()