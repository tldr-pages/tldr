# ps

> Información sobre los procesos en ejecución.
> Más información: <https://www.unix.com/man-page/osx/1/ps/>.

- Lista todos los procesos en ejecución:

`ps aux`

- Lista todos los procesos en ejecución incluyendo la cadena de comandos completa:

`ps auxww`

- Busca un proceso que coincida con una cadena:

`ps aux | grep {{cadena}}`

- Obtén el PID principal de un proceso:

`ps -o ppid= -p {{pid}}`

- Ordena los procesos por uso de memoria:

`ps -m`

- Ordena los procesos por uso de CPU:

`ps -r`
