# strace

> Herramienta de diagnóstico para rastrear llamadas al sistema.
> Más información: <https://manned.org/strace>.

- Rastrea las llamadas de un proceso usando su PID:

`strace {{[-p|--attach]}} {{pid}}`

- Rastrea un proceso y filtra la salida según [e]xpresiones de llamadas al sistema:

`strace {{[-p|--attach]}} {{pid}} -e {{llamada_sis,llamada_sis2,...}}`

- Cuenta el tiempo, número de llamada y errores para cada llamada al sistema y devuelve un resumen cuando el programa acabe:

`strace {{[-p|--attach]}} {{pid}} {{[-c|--summary-only]}}`

- Muestra el tiempo dedicado en cada llamada al sistema y especifica el tamaño máximo de cadena a imprimir:

`strace {{[-p|--attach]}} {{pid}} {{[-T|--syscall-times]}} {{[-s|--string-limit]}} {{32}}`

- Rastrea un programa ejecutándolo:

`strace {{programa}}`

- Rastrea las operaciones de archivos de un programa:

`strace -e trace=file {{programa}}`

- Rastrea las operaciones de red de un programa, así como las de todos sus procesos hijos, guardando la salida en un archivo:

`strace {{[-f|--follow-forks]}} -e trace=network {{[-o|--output]}} {{rastreo.txt}} {{programa}}`
