produtos = [
    {"nome": "Teclado", "preco": 150},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Monitor", "preco": 900},
    {"nome": "Cabo", "preco": 30}
]
quantidade = 0
total = 0

for produto in produtos:
    if produto["preco"] >= 100:
        quantidade = quantidade + 1
        total = total + produto["preco"]

print(f'Quantidade = {quantidade}')
print(f'Total = {total}')