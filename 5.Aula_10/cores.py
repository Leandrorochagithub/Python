## Comece imprimindo o código de escape especial: \033[.
#Em seguida, adicione o código de cor. Os códigos de cores têm o formato cor_texto;cor_fundo, sendo que cada parte é opcional.
#Para cores do texto, você pode usar os seguintes códigos:
#Preto: 30
#Vermelho: 31
#Verde: 32
#Amarelo: 33
#Azul: 34
#Magenta: 35
#Ciano: 36
#Branco: 37
#Para cores de fundo, você pode usar os seguintes códigos:
#Preto: 40
#Vermelho: 41
#Verde: 42
#Amarelo: 43
#Azul: 44
#Magenta: 45
#Ciano: 46
#Branco: 47
#Após o código de cor, adicione um "m" para fechar o código de escape.
#Aqui está um exemplo que imprime o texto "Olá, mundo!" em vermelho:
#
#python
#Copy code
print("\033[31mOlá, mundo!\033[m")
#Isso resultará em "Olá, mundo!" sendo exibido em vermelho no terminal.
#Você também pode combinar códigos de cor para obter diferentes combinações. Por exemplo, para exibir o texto "Olá, mundo!" em amarelo com fundo azul:
#python
#Copy code
print("\033[33;44mOlá, mundo!\033[m")
#Agora, "Olá, mundo!" será exibido em amarelo com fundo azul.
#Lembre-se de adicionar o código \033[m no final para redefinir as cores e evitar que os próximos textos também sejam afetados pela cor.
#Essa é apenas uma introdução básica às cores ANSI em Python. Existem mais opções disponíveis, como negrito, sublinhado e estilos adicionais. Você pode explorar mais códigos e combinações para obter os efeitos de cor desejados.
print('\033[7;33;4mOlá, mundo!\033]m')