def formatar_nome(nome, sobrenome, apelido=""):
    if apelido:
        full_name= nome + ' ' + sobrenome + ' ' + apelido
    else:
        full_name= nome + ' ' + sobrenome 
    return full_name.title()
