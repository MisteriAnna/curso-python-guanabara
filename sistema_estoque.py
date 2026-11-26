produtos = [
    {"nome": "Teclado", "preco": 150, "estoque": 8},
    {"nome": "Mouse", "preco": 80, "estoque": 0},
    {"nome": "Monitor", "preco": 900, "estoque": 3}
]
def verificar_estoque(estoque):
    if estoque > 0:
        return "Disponivel"
    return "Indisponivel"

def calcular_valor(produto):
    total = produto["preco"] * produto["estoque"]
    return total

def calcular_total_estoque(produtos):
    return sum(calcular_valor(produto) for produto in produtos)

for produto in produtos:
    situacao = verificar_estoque(produto["estoque"])
    total = calcular_valor(produto)

    print(f'{produto["nome"]} - {situacao} - {total}')

print(f'Valor total em estoque: {calcular_total_estoque(produtos)}')



