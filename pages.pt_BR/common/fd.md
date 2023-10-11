# fd

> Uma alternativa para `find`.
> Visa ser mais rápido e fácil de usar do que `find`.
> Mais informações: <https://github.com/sharkdp/fd>.

- Encontra recursivamente arquivos que correspondam ao padrão fornecido no diretório atual:

`fd {{padrão}}`

- Encontra arquivos que começam com `foo`:

`fd '^foo'`

- Encontra arquivos com uma extensão específica:

`fd --extension txt`

- Encontra arquivos em um diretório específico:

`fd '{{padrão}}' {{caminho/para/diretório}}`

- Inclui arquivos ignorados e ocultos na pesquisa:

`fd --hidden --no-ignore '{{padrão}}'`

- Executa um comando em cada resultado de pesquisa retornado:

`fd '{{padrão}}' --exec {{comando}}`
