'''
Adicione um método estático quantidade_pessoas que retorna a quantidade de objetos Pessoa instanciados.
Teste o método instanciando alguns objetos e verificando a quantidade.
'''

class Pessoa:
    nome = " "
    sobrenome = " "
    idade = None
    x = 0  # contador

    def __init__(self, nome_passado, sobrenome_passado, idade_passada):
        self.nome = nome_passado
        self.sobrenome = sobrenome_passado
        self.idade = idade_passada
        Pessoa.x += 1

    def imprime_dados_completos(self):
        return print(f"{self.nome} {self.sobrenome}, {self.idade} anos.")

    @staticmethod # definir um método estático em uma classe. 
    def quantidade_pessoas():
        return Pessoa.x

pessoa1 = Pessoa("Ana", "Karolyne", 16)
pessoa2 = Pessoa("Carla", "Cristina", 33)
pessoa3 = Pessoa("Junio", "Campos", 37)

pessoa1.imprime_dados_completos()
pessoa2.imprime_dados_completos()
pessoa3.imprime_dados_completos()

print(f"Quantidade de pessoas instanciadas: {Pessoa.quantidade_pessoas()}")
