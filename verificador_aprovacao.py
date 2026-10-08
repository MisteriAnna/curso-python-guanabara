alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 6.0},
    {"nome": "Maria", "nota": 9.0}
]
def verificar_aprovacao(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

for aluno in alunos:
    situacao = verificar_aprovacao(aluno["nota"])
    print(f'{aluno["nome"]} - {situacao}')
