# stdbuf

> Ejecuta un comando con operaciones de almacenamiento en búfer modificadas para sus flujos estándar.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>.

- Cambia el tamaño del búfer de `stdin` a 512 KiB:

`stdbuf {{[-i|--input]}} 512K {{comando}}`

- Cambia el búfer de `stdout` a búfer por líneas:

`stdbuf {{[-o|--output]}} L {{comando}}`

- Configura el búfer `stderr` sin almacenamiento en búfer:

`stdbuf {{[-e|--error]}} 0 {{comando}}`
