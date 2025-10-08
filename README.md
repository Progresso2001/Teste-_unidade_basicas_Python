***
<p align="center">
  <img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# Formatação de Nomes em Python

Este projeto contém um script Python para formatar nomes completos a partir de nome, sobrenome e, opcionalmente, um apelido. O nome formatado fica com a primeira letra em maiúscula de cada parte.

## Descrição

A função principal `formatar_nome` aceita três parâmetros: `nome`, `sobrenome` e `apelido` (opcional). Se o apelido for fornecido, ele será incluído no resultado final. A função retorna o nome completo formatado em formato título.

O script interativo permite que o usuário digite o nome, sobrenome e apelido, gerando a saída formatada até que o usuário digite 'q' para sair.

## Como usar

1. Execute o script principal.
2. Insira o nome, sobrenome e apelido quando solicitado.
3. Para sair, digite `q` a qualquer momento.

Exemplo:
```
Digite 'q' a qualquer momento para sair.

Porfavor digite o nome: manuel
Por favor digite o sobrenome: elias
Porfavor digite o outro apelido: 
    Ordenadamente nome formatado: Manuel Elias.
```

## Testes

O projeto inclui testes unitários usando `unittest` para validar o funcionamento da função `formatar_nome`.

Para rodar os testes:
```bash
python -m unittest nome_do_arquivo_de_teste.py
```

## Estrutura do Projeto

- `name_function.py`: Contém a função `formatar_nome`.
- Script principal: Interação com o usuário para ler nomes e formatar.
- Arquivo de testes: Casos de teste para garantir o correto funcionamento da função.

***

Ciado por : Joaquim Eliseu Menianga
