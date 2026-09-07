frase = input("Digite uma frase: ")
palavra = input("Qual palavra deseja procurar? ")

frase = frase.lower()
palavra = palavra.lower()

posicao = frase.find(palavra)

if posicao == -1:
   print("Palavra não encontrada")
else:
   print(f'Palavra encontrada na posição {posicao}')


