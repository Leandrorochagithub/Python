#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome

nome= input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count('  '))
dividido= nome.split()
print(len(dividido[0]))
