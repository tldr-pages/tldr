# cut

> Recorta campos de `stdin` ou arquivos.
> Mais informações: <https://manned.org/man/freebsd-13.0/cut.1>.

- Imprime um intervalo específico de caracteres/campos de cada linha:

`{{comando}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Imprime um intervalo de campos de cada linha com um delimitador específico:

`{{comando}} | cut -d "{{,}}" -f {{1}}`

- Imprime um intervalo de caracteres de cada linha de um arquivo específico:

`cut -c {{1}} {{caminho/para/arquivo}}`
