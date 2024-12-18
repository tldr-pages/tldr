# cut

> Corta campos de `stdin` o archivos.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- Imprime un rango específico de caracteres/campos de cada línea:

`{{comando}} | cut --{{characters|field}} {{1|1,10|1-10|1-|-10}}`

- Imprime un rango de campos de cada línea con un [d]elimitador específico:

`{{comando}} | cut --delimiter "{{,}}" --fields {{1}}`

- Imprime un rango de [c]aracteres de cada línea del archivo específico:

`cut --characters {{1}} {{ruta/al/archivo}}`

- Imprime [c]ampos específicos de líneas terminadas en `NUL` (por ejemplo, como en `find . -print0`) en lugar de nuevas líneas:

`{{comando}} | cut --zero-terminated --fields {{1}}`
