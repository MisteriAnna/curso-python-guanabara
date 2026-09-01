nome = input("Nome do aluno ")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("ERRO: as notas devem estar entre 0 e 10.")


else:
    media = (nota1 + nota2) / 2

    print(f'{nome} ficou com a média {media:.1f}')

    if media >= 7:
        print("APROVADO")
    elif media < 5:
        print("REPROVADO")
    else:
        print("RECUPERAÇÃO")