# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

ex_primitivo = input('Digite algo: ')

print('O tipo primitivo da palavra digitada é {}'.format(type(ex_primitivo)))
print('Só tem espaços? {}'.format(ex_primitivo.isspace()))
print('Esta capitalizada? {}'.format(ex_primitivo.istitle()))
print('A palavra digitada esta toda em maiúscula? {}'.format(ex_primitivo.isupper()))
print('A palavra digitada esta toda em minúscula ? {}'.format(ex_primitivo.islower()))
print('A palavra digitada é alfabética ? {}'.format(ex_primitivo.isalpha()))
print('A palavra digitada é Alfanumérica - letras e/ou números - ? {}'.format(ex_primitivo.isalnum()))
print('A palavra digitada só possui números ? {}'.format(ex_primitivo.isnumeric()))

