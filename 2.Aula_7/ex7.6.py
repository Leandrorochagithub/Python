salarioatual=float(input('Digite o salario atual: '))
aumento=int(input('Digite o acréscimo em porcentagem: '))
aumentocalc=aumento/100
aumentoresult=(salarioatual*aumentocalc)
salariofuturo=salarioatual+aumentoresult
print('O salário atual é de {}, com acréscimo de {}%, o aumento será de {} e o salário futuro será de {}.'.format(salarioatual, aumento,aumentoresult,salariofuturo))