tecnologias = ["python", "git", "sql"]
nova = input("Digite uma nova tecnologia: ")
nova = nova.lower()

if nova in tecnologias:
   print("Tecnologia já cadastrada.")
else:
   tecnologias.append(nova)
   print("Tecnologia adicionada ")
   print(tecnologias)

#for numero in range (0, 5):
   #tecnologia = input("Digite a tecnologia que voce quer aprender: ")
  # tecnologias.append(tecnologia)

#print("Voce quer aprender: ")
#for numero in range (0, 5):
   #print((numero + 1), tecnologias[numero])





