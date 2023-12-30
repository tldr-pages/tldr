# cortar

> Corta campos de `stdin` o archivos.
> Más información: <https://www.gnu.org/software/coreutils/cut>.

- Imprime un rango específico de caracteres/campos de cada línea:

`{{command}} | cut --{{caracteres|campos}}={{1|1,10|1-10|1-|-10}}`

- Imprime un rango de cada línea con un delimitador específico:

`{{command}} | cut --delimiter="{{,}}" --{{campos}}={1}}`

- Imprime un rango de cada línea del archivo específico:

`cut --{{caracteres}}={{1}} {{ruta/al/archivo}}`
