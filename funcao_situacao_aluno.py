nome = input(f'Digite o nome: ')
nota = float(input(f'Digite a nota: '))
def mostrar_situacao(nome, nota):
    if nota >= 7:
        print(f'{nome} - Aprovado')
    else:
        print(f'{nome} - Reprovado')

mostrar_situacao(nome, nota)