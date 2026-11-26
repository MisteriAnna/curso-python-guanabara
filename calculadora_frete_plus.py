def calcular_desconto(valor):
    if valor >= 500:
        return valor * 0.2

    if valor >= 200:
        return valor * 0.1

    return 0

def calcular_total(valor, desconto):
    return valor - desconto

valor = float(input(f'Digite o valor da compra: '))

while valor < 0:
    print("Digite um valor de compra positivo.")
    valor = float(input("Valor: "))

desconto = calcular_desconto(valor)
total =  calcular_total(valor, desconto)

print(f'Compra: R$ {valor:.2f}')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Total: R$ {total:.2f}')