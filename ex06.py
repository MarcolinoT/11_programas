#6- Escrever um algoritmo que lê o número de identificação, 
#as 3 notas obtidas por um aluno nas 3 verificações e a média dos
#exercícios que fazem parte da avaliação. Calcular a média de aproveitamento,
#usando a fórmula:
#MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
#O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, 
#a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o 
#conceito for A, B ou C e REPROVADO se o conceito for D ou E. Pergunte se o usuário 
#deseja digitar as notas de outro aluno S para sim e N para não

while True:
    Nome = input('digite seu nome:')
    Ra = input('digite seu número de identificação:')
    N1 = float(input('digite a nota 1:'))
    N2 = float(input('digite a nota 2:'))
    N3 = float(input('digite a nota 3:'))
    ME = float(input('digite a nota ME:'))
    print('-'*70)

    MA = (N1 + (N2*2) + (N3*3) + ME)/7


    if MA >= 9.0:
        conceito = 'A'
        
    elif 7.5 <= MA < 9.0:
        conceito = 'B'
        
    elif 6.0 <= MA < 7.5:
        conceito = 'C'
        
    elif 4.0 <= MA < 6.0:
        conceito = 'D'
        
    elif MA < 4.0:
        conceito = 'E'
    
    if conceito in ['A','B','C']:
        Aprovação ='Aprovado'
    elif conceito in ['D','E']:
        Aprovação = 'Reprovado'    

    print(f"Nome do Aluno:{Nome}")
    print(f"RA do aluno: {Ra} ")
    print(f"Notas: Nota1:{N1}, Nota2:{N2}, Nota3:{N3} ")
    print(f"Média dos exercícios: {ME} ")
    print(f"Média de aproveitamento: {MA} ")
    print(f"Conceito: {conceito} ")
    print(f"Aprovação: {Aprovação} ")

    Retorno = input("Deseja digitar as notas de outro aluno? (S/N): ")
    if Retorno.upper() != "S":
        break

    



