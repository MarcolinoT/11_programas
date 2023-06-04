#5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliações. 
quantidade = int(input('digite a quantidade de notas:'))
soma = 0
contador = 1
for i in range(quantidade):
    notas = float(input(f'Nota {contador}:'))
    soma = soma + notas
    contador +=1
    média = soma/quantidade
print(f'Sua média foi de:{média}')    
    