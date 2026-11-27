def calcular_valor(produto):
    total = produto["preco"] * produto["estoque"]
    print(total)

produto = {
    "nome": "Teclado",
    "preco": 150,
    "estoque": 8
}

resultado = calcular_valor(produto)
print(resultado)

