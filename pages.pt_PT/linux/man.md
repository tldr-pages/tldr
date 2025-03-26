# man

> Formata e exibe páginas do manual.
> Mais informações: <https://manned.org/man>.

- Exibe a página do manual para um comando:

`man {{comando}}`

- Exibe a página do manual para um comando da seção 7:

`man {{7}} {{comando}}`

- Lista todas as seções disponíveis para um comando:

`man {{[-f|--whatis]}} {{comando}}`

- Exibe o caminho pesquisado para páginas do manual:

`man {{[-w|--path]}}`

- Exibe a localização de uma página do manual em vez da página em si:

`man {{[-w|--where]}} {{comando}}`

- Exibe a página do manual usando uma localização específica:

`man {{[-L|--locale]}} {{localização}} {{comando}}`

- Procura por páginas do manual que contenham uma certa string:

`man {{[-k|--apropos]}} "{{string_buscada}}"`
