tentativas = 1
senha = input("Senha: ")

while senha != 'python123':
    print("Senha incorreta.")
    if tentativas >= 3:
        print('Acabaram as tentativas.')
        break
    tentativas = tentativas + 1
    senha = input("Senha: ")


if senha == 'python123':
    print("Acesso permitido!")
else:
    print("Acesso bloqueado!")


