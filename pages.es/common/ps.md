# ps

> Información sobre procesos en ejecución.
> Más información: <https://manned.org/ps>.

- Lista todos los procesos en ejecución:

`ps aux`

- Lista todos los procesos en ejecución incluyendo el comando completo:

`ps auxww`

- Busca un proceso que coincida con la cadena de texto:

`ps aux | grep {{cadena}}`

- Lista todos los procesos del usuario actual en formato supercompleto:

`ps {{[-u|--user]}} $(id {{[-u|--user]}}) -F`

- Lista todos los procesos del usuario actual como un árbol:

`ps {{[-u|--user]}} $(id {{[-u|--user]}}) f`

- Obtén el PID del proceso padre:

`ps {{[-o|--format]}} ppid= {{[-p|--pid]}} {{pid}}`

- Ordena los procesos por consumo de memoria:

`ps --sort size`
