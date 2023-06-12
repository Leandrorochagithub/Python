#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint #Sortear número inteiro aleatório
from time import sleep #Dar uma pausa na geração do código
computador= randint(0,5)
print('=='*20)
print('Eu pensei em um número entre 0 e 5. Tente advinhar...')
print('==' *20)
jogador= int(input('Em que número eu pensei?'))
if jogador == computador:
    print('PROCESSANDO...')
sleep(3) #3 se. de pausa
print('Você acertou. Parabéns!')
print('Eu pensei no número...{}!'.format(computador))
print('Voce errou. Tente novamente!')