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

`ps --user $(id -u) -F`

- Lista todos los procesos del usuario actual como un árbol:

`ps --user $(id -u) f`

- Obtén el PID del proceso padre:

`ps -o ppid= -p {{pid}}`

- Ordena los procesos por consumo de memoria:

`ps --sort size`
