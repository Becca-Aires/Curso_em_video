'''Crie um script Python que leia o dia, o mês e o ano de nascimento de 
uma pessoa e mostra uma mensagem com a data formatada.'''

dia = int(input('Informe o dia do seu nascimento: '))
mês = input('Informe o mês que você nasceu: ') #no py, já é automático a string, então não precisa determinar
ano = int(input('Informe o ano que você nasceu: '))

print('Você nasceu dia',dia,'de',mês,'de',ano,'. Certo?')