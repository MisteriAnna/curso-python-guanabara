email = input(f"Digite seu email: ")

if email.count("@") == 1 and "." in email:
   print(f'{email} Email válido')
else:
   print(f'{email} Email inválido')

