#2- Faça um programa que leia um nome de usuário e sua senha 
#e não aceite a senha igual ao nome do usuário, mostrando 
#uma mensagem de erro e retornando a pedir as informações.

nome=input('Digite seu nome:')
senha=input("Digite uma senha:")
while nome == senha:
    print('Sua senha não pode ser igual ao seu nome, digite uma nova senha:')
    senha=(input("Digite uma senha:"))
print('Nome e senha cadastrado com sucesso.')     