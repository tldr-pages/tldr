# man

> Formata e exibe páginas de manual.
> Mais informações: <https://manned.org/man>.

- Exibe a página de manual de um comando:

`man {{comando}}`

- Abre uma página de manua para um comando em um navegadore de internet (a variável de ambiente `BROWSER` pode subistituir `=nome_do_navegador`):

`man {{[-Hnome_do_navegador|--html=nome_do_navegador]}} {{command}}`

- Exibe a página de manual de um comando da seção 7:

`man {{7}} {{comando}}`

- Lista todas as seções disponíveis para um comando:

`man {{[-f|--whatis]}} {{comando}}`

- Exibe o caminho procurado pelas páginas de manual:

`man {{[-w|--path]}}`

- Exibe a localização de uma página de manual em vez da própria página de manual:

`man {{[-w|--where]}} {{comando}}`

- Exibe a página de manual usando uma localidade específica:

`man {{[-L|--locale]}} {{localicade}} {{comando}}`

- Procura páginas de manual contendo um termo de pesquisa:

`man {{[-k|--apropos]}} "{{termo_de_pesquisa}}"`
