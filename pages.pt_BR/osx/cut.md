# cut

> Recortar campos de stdin ou arquivos.
> Mais informações: <https://manned.org/man/freebsd-13.0/cut.1>.

- Imprimir um intervalo específico de caracteres/campos de cada linha:

`{{comando}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Imprimir um intervalo de cada linha com um delimitador específico:

`{{comando}} | cut -d "{{,}}" -{{c}} {{1}}`

- Imprimir um intervalo de cada linha de um arquivo específico:

`cut -{{c}} {{1}} {{caminho/para/arquivo}}`
