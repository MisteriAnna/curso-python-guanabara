alunos = []

for numero in range(3):
    nome = input("Nome: ")
    nota = float(input("Nota: "))

    while nota < 0 or nota > 10:
        print("Nota inválida")
        nota = float(input("Nota: "))

    aluno = {
        "nome": nome,
        "nota": nota
    }
    alunos.append(aluno)

aprovados = 0

for aluno in alunos:
    if aluno["nota"] >=7:
        print(f'{aluno["nome"]} - Aprovado')
        aprovados = aprovados + 1
    else:
        print(f'{aluno["nome"]} - Reprovado')

print(f'Quantidade de aprovados: {aprovados}')





