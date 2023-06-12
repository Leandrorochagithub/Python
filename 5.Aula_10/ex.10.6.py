#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
import random
n1= random.randint(0,1000)
n2= random.randint(0,1000)
n3= random.randint(0,1000)
maiorN= max(n1,n2,n3)
menorN= min(n1,n2,n3)
print('Dos valores {}, {} e {}. O maior é {} e o menor número é {}'.format(n1,n2,n3,maiorN, menorN) )