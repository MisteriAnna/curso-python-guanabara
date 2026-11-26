produtos = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 900}
]
def classificar_preco(preco):
    if preco >= 500:
        return "Muito caro"
    elif preco >= 100:
        return "Caro"
    else:
        return "Barato"

for produto in produtos:
    situacao = classificar_preco(produto["preco"])
    print(f'{produto["nome"]} - {situacao}')