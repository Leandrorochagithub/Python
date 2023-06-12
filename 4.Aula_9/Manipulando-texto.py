#frase= 'Curso em video' 
#print(frase[::2]) #Croe ie - da 0 até o final, pulando de 2 em 2 
#print(frase[3:10]) # so em v - entre 3 e 10, não mostra a 10
#print(frase[:3]) # Cur - da 0 até 3
#print(frase[12:]) # eo - da 12 até o final
#print(frase[2:10:2]) #roe da 2 até a 10, pulando de 2 em 2

texto= 'Aprendendo Python'
print(texto.count('o')) #2
print(texto.upper().count('O')) #2
print(len(texto)) #17
print(texto.strip()) #2 - tira espaços iniciais e finais desnecessários ( lstrip-left/rstrip-rigth)
print(texto.replace('Python', 'JS')) # Aprendendo JS
print('Python' in texto) #True
print(texto.lower().find('Aprendendo')) #-1 = false - Aprendendo tem A
print(texto.find('Aprendendo')) # 0 = True
print(texto.split())# lista separando as palavras ['Aprendendo', 'Python']
dividido= texto.split()
print(dividido[1])