# procstat

> Muestra información detallada sobre los procesos en FreeBSD.
> Más información: <https://man.freebsd.org/cgi/man.cgi?query=procstat>.

- Muestra los descriptores de archivo de un proceso específico:

`procstat fds {{pid}}`

- Muestra las asignaciones de memoria virtual de un proceso:

`procstat vm {{pid}}`

- Muestra los argumentos de un proceso:

`procstat arguments {{pid}}`

- Muestra los límites de recursos de un proceso:

`procstat rlimit {{pid}}`
