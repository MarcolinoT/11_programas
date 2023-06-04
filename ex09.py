#9- Uma concessionária de veículos está vendendo os seus veículos com desconto. 
#Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago 
#pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano 
#do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se 
#deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar 
#total de carros com ano até 2000 e total geral.

while True:
    Ano = int(input('Digite o ano do carro que deseja comprar:'))
    valor = float(input('Informe o valor original do carro:'))
    if Ano <=2000:
        desconto = valor*(0.12)
        novovalor = valor - desconto
        print(f'O carro de R${valor}, com o desconto de 12% (R${desconto}), saira por R${novovalor}')
    else:
        desconto= valor*(0.07)
        novovalor = valor - desconto
        print(f'O carro de R${valor}, com o desconto de 12% (R${desconto}), saira por R${novovalor}')

    retorno = input('Deseja fazer outra consulta? S/N?')
    if retorno.upper() != "S":
        break


