# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Qual a distância a ser percorrida?"))
precoAte200 = 0.50
precoMais200 = 0.45

if distancia <= 200:
    print('O valor a ser pago é de {:.2f} reais!'.format(distancia * precoAte200))
else:
    print('O valor a ser pago é de {:.2f} reais!'.format(distancia * precoMais200))

