produtos = [
    {"nome": "Teclado", "preco": 150, "estoque": 8},
    {"nome": "Mouse", "preco": 80, "estoque": 0},
    {"nome": "Monitor", "preco": 900, "estoque": 3},
    {"nome": "Webcam", "preco": 200, "estoque": 2}
]
def encontrar_mais_caro(produtos):
    mais_caro = produtos[0]
    for produto in produtos:
        if produto["preco"] > mais_caro["preco"]:
            mais_caro = produto
    return mais_caro

resultado = encontrar_mais_caro(produtos)
print(resultado["nome"])
print(resultado["preco"])