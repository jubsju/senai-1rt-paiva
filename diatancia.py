Distancia = float(input("digite a distancia da viagem em km:"))

if Distancia <= 200:
    preco = Distancia * 0.50
else:
    preco = Distancia * 0.45

print("O preço da passagem é R$ {:.2f}".format(preco))
