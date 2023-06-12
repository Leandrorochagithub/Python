# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n=int(input('Digite um número inteiro:'))
if n%2 == 0: # Se o resto da divisão do valor por 2 = 0(par). Se for =1(ímpar)
    print('{} é um número par!'.format(n))
else:
    print('{} é um número ímpar!.'.format(n))