# cut

> Corta campos de `stdin` o archivos.
> Más información: <https://www.gnu.org/software/coreutils/cut>.

- Imprime un rango específico de caracteres/campos de cada línea:

`{{comando}} | cut --{{characters|field}} {{1|1,10|1-10|1-|-10}}`

- Imprime un rango de campos de cada línea con un delimitador específico:

`{{comando}} | cut --delimiter="{{,}}" --fields {{1}}`

- Imprime un rango de caracteres de cada línea de un archivo específico:

`cut --characters {{1}} {{ruta/al/archivo}}`
