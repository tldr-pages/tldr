# cut

> Corta campos sean `stdin` o archivos.
> Más información: <https://manned.org/man/freebsd-13.0/cut.1>.

- Imprime un rango específico de caracteres/campos de cada línea:

`{{command}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Imprime un rango de campos de cada línea con un delimitador específico:

`{{command}} | cut -d "{{,}}" -f {{1}}`

- Imprime un rango de caracteres de cada línea de un archivo específico:

`cut -c {{1}} {{ruta/al/archivo}}`
