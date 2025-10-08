from name_function import formatar_nome

print("Digite 'q' a qualquer momento para sair.")

while True:
    nome = input("\nPorfavor digite o nome: ")
    if nome == 'q':
        break
    sobrenome = input("\NPor favor digite o sobrenome: ")
    if sobrenome == 'q':
        break
    apelido=input("Porfavor digite o outro apelido: ")
    if apelido == 'q':
        break
    nome_formatado = formatar_nome(nome, sobrenome, apelido)
    print("\tOrdenadamente nome formatado: " + nome_formatado + ".")

