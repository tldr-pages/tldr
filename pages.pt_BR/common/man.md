# man

> Formata e exibe páginas de manual.
> Mais informações: <https://www.manned.org/man>.

- Exibe a página de manual de um comando:

`man {{comando}}`

- Exibe a página de manual de um comando da seção 7:

`man {{7}} {{comando}}`

- Lista todas as seções disponíveis para um comando:

`man -f {{comando}}`

- Exibe o caminho procurado pelas páginas de manual:

`man --path`

- Exibe a localização de uma página de manual em vez da própria página de manual:

`man -w {{comando}}`

- Exibe a página de manual usando uma localidade específica:

`man {{comando}} --locale={{localidade}}`

- Procura páginas de manual contendo um termo de pesquisa:

`man -k "{{termo_de_pesquisa}}"`
