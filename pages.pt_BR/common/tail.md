# tail

> Exibe a parte final de um arquivo.
> Veja também: `head`.
> Mais informações: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Mostra as últimas 'contagem' linhas de um arquivo:

`tail {{[-n|--lines]}} {{contagem}} {{caminho/para/arquivo}}`

- Exibe um arquivo a partir de um número de linha específico:

`tail {{[-n|--lines]}} +{{contagem}} {{caminho/para/arquivo}}`

- Mostra uma quantidade específica de bytes a partir do final de um arquivo:

`tail {{[-c|--bytes]}} {{contagem}} {{caminho/para/arquivo}}`

- Exibe as últimas linhas de um arquivo e continua lendo até pressionar `<Ctrl c>`:

`tail {{[-f|--follow]}} {{caminho/para/arquivo}}`

- Continua lendo um arquivo até `<Ctrl c>`, mesmo que ele fique inacessível:

`tail {{[-F|--retry --follow]}} {{caminho/para/arquivo}}`

- Mostra as últimas 'num' linhas de um arquivo e atualiza a cada 'n' segundos:

`tail {{[-n|--lines]}} {{contagem}} {{[-s|--sleep-interval]}} {{segundos}} {{[-f|--follow]}} {{caminho/para/arquivo}}`
