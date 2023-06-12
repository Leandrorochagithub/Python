#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade= int(input('Em que velocidade o carro está (km/h)?'))
calculoLimiteAcima= (velocidade-80)
multa= (velocidade-80)*7
if velocidade < 80:
    print('O carro está dentro do limite permitido de 80 km/h!')
else:
    print('O carro está a {} KM/h. {} Km/h acima do limite permitido!'.format(velocidade,calculoLimiteAcima))
    print('Valor da multa: R$ {:.2f}! '.format(multa)) #2 casas decimais flutuantes 