temperaturas = [22.5, 19.0, 25.5, 30.0, 18.5, 27.0, 21.5]
media = sum(temperaturas) / len(temperaturas)
acima_da_media = []

for temperatura in temperaturas:
   if temperatura > media:
      acima_da_media.append(temperatura)

print("Menor temperarura: ", min(temperaturas))
print("Maior Temperatura: ", max(temperaturas))
print("Média: ", round((media), 2))
print("Temperaturas acima da média: ", (acima_da_media))