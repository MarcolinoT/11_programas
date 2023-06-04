#10 Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número
n = int(input("Digite a quantidade de números a serem verificados: "))
contador = 1
for i in range(n):
    numero = float(input(f"Digite o {contador}° número: "))
    contador +=1

    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")

    print('-'*30)    
