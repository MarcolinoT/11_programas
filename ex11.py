#11- Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. 
#Mostre como resultado se houve lucro, prejuízo ou empate para cada produto.
# Informe a média de preço de custo e do preço de venda.
soma_venda=0
soma_custo=0

for i in range (1,40):    
    custo= float(input(f'informe o preço de custo do produto {i}:'))
    venda = float(input(f'Informe o preço de venda do produto {i}:'))

    soma_venda = soma_venda + custo
    soma_custo = soma_custo + venda

    media_venda = soma_venda/i
    media_custo = soma_custo/i 

    if custo == venda:
        print("Não ouve lucro nem perda na venda")
    elif custo > venda:
        print("teve perca na venda desse produto")
    elif custo < venda:
        print("Teve lucro nesse produto")    

    print('----------------------------------------------------------')     

print(f'A média de preço de venda foi de: R${media_venda}')
print(f'A média de preço de custo foi de: R${media_custo}')           
