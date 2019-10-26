# touch

> Atualizar as timestamps dos ficheiro para a hora atual.
> Se o ficheiro não existir, cria ficheiro vazio, a menos que seja passado parâmetro -c ou -h.

- Cria novo(s) ficheiro(s) vazio ou atualiza as timestamps para a hora atual:

`touch {{ficheiro}}`

- Define as timestamps de um ficheiro para a hora especificada:

`touch -t {{YYYYMMDDHHMM.SS}} {{nome_ficheiro}}`

- Usa as timestamps do ficheiro1 para definir as horas do ficheiro2:

`touch -r {{ficheiro1}} {{ficheiro2}}`

- Altera as timestamps de um ficheiro. Não cria novo ficheiro se não existir:

`touch -c {{ficheiro}}`
