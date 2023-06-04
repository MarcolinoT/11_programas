#8- Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.
for i in range(1,6):
    idade = int(input(f'Digite a idade da pessoa {i}:'))
    if idade >= 18:
        print('Maior de idade')
    else:
        print('Menor de idade')                  