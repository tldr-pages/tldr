# gdu

> Analisador de uso de disco com interface de console.
> Mais informações: <https://github.com/dundee/gdu>.

- Exibe interativamente o uso de disco do diretório atual:

`gdu`

- Exibe interativamente o uso de disco de um determinado diretório:

`gdu {{caminho/para/diretório}}`

- Exibe interativamente o uso de disco de todos os discos montados:

`gdu --show-disks`

- Exibe interativamente o uso de disco do diretório atual, mas ignora alguns subdiretórios:

`gdu --ignore-dirs {{caminho/para/diretório1,caminho/para/diretório2,...}}`

- Ignora caminhos por expressão regular:

`gdu --ignore-dirs-pattern '{{.*[abc]+}}'`

- Ignora diretórios ocultos:

`gdu --no-hidden`

- Imprime apenas o resultado, não entra no modo interativo:

`gdu --non-interactive {{caminho/para/diretório}}`

- Não mostra o progresso no modo não interativo (útil em scripts):

`gdu --no-progress {{caminho/para/diretório}}`
