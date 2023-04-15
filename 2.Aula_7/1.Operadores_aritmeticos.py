#+	Adição	Realiza a soma de ambos operandos.
#-	Subtração	Realiza a subtração de ambos operandos.
# (*	Multiplicação	Realiza a multiplicação de ambos operandos.
#/	Divisão	Realiza a Divisão de ambos operandos.
# (//	Divisão inteira	Realiza a divisão entre operandos e a parte decimal de ambos operandos.
#%	Módulo	Retorna o resto da divisão de ambos operandos.
# (** Exponenciação	Retorna o resultado da elevação da potência pelo outro

quatro = 4
dois = 2

soma = quatro + dois
print(soma)  # Resultado: 6

subtracao = quatro - dois
print(subtracao)  # Resultado: 2

multiplicacao = quatro * dois
print(multiplicacao)  # Resultado: 8

divisao = quatro / dois
print(divisao)  # Resultado: 2.0

divisao_interna = quatro // dois
print(divisao_interna)  # Resultado: 2

modulo = quatro % dois
print(modulo)  # Resultado: 0

exponenciacao = quatro ** dois
print(exponenciacao)  # Resultado: 16

#==	Igual a	Verifica se um valor é igual ao outro
# (!=	Diferente de	Verifica se um valor é diferente ao outro
#>	Maior que	Verifica se um valor é maior que outro
#>=	Maior ou igual	Verifica se um valor é maior ou igual ao outro
#<	Menor que	Verifica se um valor é menor que outro
#<=	Menor ou igual	Verifica se um valor é menor ou igual ao outro

var = 5

if var == 5:
    print('Os valores são iguais')

if var != 7:
    print('O valor não é igual a 7')

if var > 2:
    print('O valor da variável é maior de 2')

if var >= 5:
    print('O valor da variável é maior ou igual a 5')

if var < 7:
    print('O valor da variável é menor que 7')

if var <= 5:
    print('O valor da variável é menor ou igual a 5')

#=	x = 1
#+=	x = x + 1
#-=	x = x - 1
#(*=	x = x * 1
#/=	x = x / 1
#%=	x = x % 1

numero = 5

numero += 7
print(numero)  # Resultado será 10

#and	Retorna True se ambas as afirmações forem verdadeiras
#or	Retorna True se uma das afirmações for verdadeira
#not	retorna Falso se o resultado for verdadeiro
#is	Retorna True se ambas as variáveis são o mesmo objeto
#is not	Retorna True se ambas as variáveis não forem o mesmo objeto

lista = [1, 2, 3]
outra_lista = [1, 2, 3]
recebe_lista = lista

# Recebe True, pois são o mesmo objeto
print(f"São o mesmo objeto? {lista is recebe_lista}")

# Retorna False, pois são objetos diferentes
print(f"São o mesmo objeto? {lista is outra_lista}")

#in	Retorna True caso o valor seja encontrado na sequência
#not in	Retorna True caso o valor não seja encontrado na sequência

lista = ["Python", 'Academy', "Operadores", 'Condições']

# Verifica se existe a string dentro da lista
print('Python' in lista)  # Saída: True

# Verifica se não existe a string dentro da lista
print('SQL' not in lista) # Saída: True

nome=input('Qual o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))#Prazer em te conhecer, Leandro!
print('Prazer em te conhecer, {:>20}!'.format(nome))#Prazer em te conhecer,              Leandro!
print('Prazer em te conhecer, {:<20}!'.format(nome)) #Prazer em te conhecer, Leandro             !
print('Prazer em te conhecer, {:=^20}!'.format(nome))#Prazer em te conhecer, ======Leandro=======!
print('Prazer em te conhecer, {:^20}!'.format(nome))#Prazer em te conhecer,       Leandro       !

n1=int(input('Digite um valor: '))
n2=int(input('Digite um valor: '))
d= n1/n2
print('{}'.format(d)) #0.5
print('{:3f}'.format(d)) #0.500