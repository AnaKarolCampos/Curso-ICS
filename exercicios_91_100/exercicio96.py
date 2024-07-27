''' Crie uma nova classe Estudante que herda de Pessoa e adicione um novo atributo curso.
Adicione um método que retorna o curso do estudante.
Instancie um objeto Estudante e teste os métodos herdados e novos. '''

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
    
class Estudante(Pessoa):
    def __init__(self, nome_passado, sobrenome_passado, idade_passada, curso):
        super().__init__(nome_passado, sobrenome_passado, idade_passada) 
        self.curso = curso

    def saber_curso(self): # método
        return self.curso

pessoa1 = Estudante("Ana", "Karolyne", 16, "Eng. de Software") # instanciar obj. de Estudante

pessoa1.imprime_dados_completos()

print(f"Curso: {pessoa1.saber_curso()}") # testar saber_curso da classe Estudante

'''
A função super() é usada para chamar um método da classe base (classe pai)
a partir de uma classe derivada (classe filha).
 Neste caso, super().__init__(...) chama o construtor da classe Pessoa.
'''