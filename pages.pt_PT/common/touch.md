# touch

> Atualizar as timestamps de um ficheiro para a hora atual.
> Se o ficheiro não existir, cria um ficheiro vazio, a menos que seja passado o parâmetro -c ou -h.
> Mais informações: <https://manned.org/man/freebsd-13.1/touch>.

- Cria um novo ficheiro vazio, ou atualizar as timestamps para a hora atual:

`touch {{caminho/para/ficheiro1 caminho/para/ficheiro2 ...}}`

- Define as timestamps de um ficheiro para a hora especificada:

`touch -t {{YYYYMMDDHHMM.SS}} {{caminho/para/ficheiro1 caminho/para/ficheiro2 ...}}`
