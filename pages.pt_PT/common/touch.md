# touch

> Atualizar as timestamps de um ficheiro para a hora atual.
> Se o ficheiro não existir, cria um ficheiro vazio, a menos que seja passado o parâmetro -c ou -h.

- Criar um novo ficheiro vazio, ou atualizar as timestamps para a hora atual:

`touch {{ficheiro}}`

- Define as timestamps de um ficheiro para a hora especificada:

`touch -t {{YYYYMMDDHHMM.SS}} {{ficheiro}}`

- Usa as timestamps do ficheiro1 para definir as timestamps do ficheiro2:

`touch -r {{ficheiro1}} {{ficheiro2}}`

- Altera as timestamps de um ficheiro. Não cria novo ficheiro se não existir:

`touch -c {{ficheiro}}`
