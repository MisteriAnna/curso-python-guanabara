def calcular_frete(valor):
    if valor >= 200:
        return 0

    if valor >= 100:
        return 10

    return 20

valor = float(input(f'Digite o valor da compra: '))

while valor < 0:
    print("Digite um valor de compra positivo.")
    valor = float(input("Valor: "))

frete = calcular_frete(valor)
total = frete + valor

print(f'Compra: R$ {valor:.2f}')
print(f'Frete: R$ {frete:.2f}')
print(f'Total: R$ {total:.2f}')