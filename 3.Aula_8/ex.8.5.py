#import random
#aluno1= 'Maria'
#aluno2='João'
#aluno3='Pedro'
#aluno4='Luana'
#lista= [aluno1,aluno2,aluno3,aluno4]
#print(random.choice(lista))

import random
n1= input('Digite o nome do primeiro aluno: ')
n2= input('Digite o nome do segundo aluno: ')
n3= input('Digite o nome do terceiro aluno: ')
n4= input('Digite o nome do quarto aluno: ')
lista=[n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print( lista)