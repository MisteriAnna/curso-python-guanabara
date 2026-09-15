nome = input(f'Nome:')
idade = input(f'Idade:')
nota = float(input(f'Nota:'))

aluno = {
    "nome": nome,
    "idade": idade,
    "nota": nota
}

if nota >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')



