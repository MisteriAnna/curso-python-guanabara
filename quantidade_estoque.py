def ler_estoque():
        while True:
            try:
                estoque = int(input("Quantidade em estoque? "))

                if estoque < 0:
                    print("O estoque não pode ser negativo")
                else:
                    return estoque
            except ValueError:
                print ("Digite um número válido.")
estoque = ler_estoque()
print(f"Estoque cadastrado: {estoque}")