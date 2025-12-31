# look

> Exibe linhas começando com um prefixo em um arquivo ordenado.
> Veja também: `grep`, `sort`.
> Mais informações: <https://man.freebsd.org/cgi/man.cgi?look>.

- Busca por linhas começando com um prefixo específico em um arquivo específico:

`look {{prefixo}} {{caminho/para/arquivo}}`

- Busca sem distinção entre maiúsculas e minúsculas apenas em caracteres alfanuméricos:

`look {{[-f|--ignore-case]}} {{[-d|--alphanum]}} {{prefixo}} {{caminho/para/arquivo}}`

- Especifica um caractere de término de string (espaço por padrão):

`look {{[-t|--terminate]}} {{,}}`

- Busca em `/usr/share/dict/words` (`--ignore-case` e `--alphanum` são assumidos):

`look {{prefixo}}`
