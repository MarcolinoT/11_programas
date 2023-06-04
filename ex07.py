#7- Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).
contador = 0
for i in range(80):
    Numero = int(input('Digite um número:'))
    if Numero > 9 and Numero < 151:
        contador +=1
print(f'{contador} numeros estão no intervalo entre 10 e 150')

