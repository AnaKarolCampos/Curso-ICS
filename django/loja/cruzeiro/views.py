from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):
    dados = {
    "camisas": [
        {"nome": "Camisa Oficial 2024 - Masculina", "preco": 249.90, "tamanhos": ["P", "M", "G", "GG"], "estoque": 50},
        {"nome": "Camisa Oficial 2024 - Feminina", "preco": 249.90, "tamanhos": ["P", "M", "G"], "estoque": 30},
        {"nome": "Camisa Retrô 2003 - Unissex", "preco": 199.90, "tamanhos": ["P", "M", "G", "GG"], "estoque": 20}
    ],
    "acessorios": [
        {"nome": "Boné Cruzeiro - Azul", "preco": 59.90, "cores": ["Azul"], "estoque": 100},
        {"nome": "Chaveiro Escudo", "preco": 19.90, "material": "Metal", "estoque": 200},
        {"nome": "Caneca Cruzeiro", "preco": 34.90, "cores": ["Azul", "Branco"], "estoque": 150}
    ],
    "itens_para_casa": [
        {"nome": "Almofada Cruzeiro", "preco": 49.90, "dimensoes": "40x40cm", "estoque": 40},
        {"nome": "Copo Térmico", "preco": 79.90, "capacidade": "500ml", "estoque": 60},
        {"nome": "Toalha de Banho Cruzeiro", "preco": 89.90, "dimensoes": "140x70cm", "estoque": 70}
    ],
    "infantil": [
        {"nome": "Camisa Oficial Infantil 2024", "preco": 149.90, "tamanhos": ["2", "4", "6", "8", "10"], "estoque": 35},
        {"nome": "Body Bebê Cruzeiro", "preco": 59.90, "tamanhos": ["P", "M", "G"], "estoque": 25}
    ]
}

    return render(request, 'produtos.html', dados)

def contato(request):
    return render(request, 'contato.html')