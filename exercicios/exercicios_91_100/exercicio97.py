'''
Crie uma nova classe Trabalhador que herda de Pessoa e adicione um novo atributo empresa.
Adicione um método que retorna a empresa onde a pessoa trabalha.
Instancie um objeto Trabalhador e teste os métodos herdados e novos.
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
    
class Trabalhador(Pessoa):
    def __init__(self, nome_passado, sobrenome_passado, idade_passada, empresa):
        super().__init__(nome_passado, sobrenome_passado, idade_passada) 
        self.empresa = empresa

    def saber_empresa(self): # método
        return self.empresa

pessoa1 = Trabalhador("Ana", "Karolyne", 16, "Tal de Tal") # instanciar obj. de Trabahador

pessoa1.imprime_dados_completos()

print(f"Empresa: {pessoa1.saber_empresa()}") # testar saber_curso da classe Trabalhador

'''
A função super() é usada para chamar um método da classe base (classe pai)
a partir de uma classe derivada (classe filha).
 Neste caso, super().__init__(...) chama o construtor da classe Pessoa.
'''