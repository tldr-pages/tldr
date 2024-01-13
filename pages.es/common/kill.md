# kill

> Envía una señal a un proceso, usualmente relacionado a detener el proceso.
> Kill envia una señal para terminar uno o un grupo de procesos.
> Más información: <https://manned.org/kill.1posix>.

- Termina un programa usando la señal SIGTERM (terminar) por defecto:

`kill {{id_del_proceso}}`

- Lista todas las señales disponibles (para ser utilizadas sin el prefijo `SIG`):

`kill -l`

- Termina una tarea en segundo plano:

`kill %{{id_de_tarea}}`

- Termina un programa usando la señal SIGHUP (hang up/colgar). Muchos programas residentes se recargarán en lugar de terminar:

`kill -{{1|HUP}} {{id_del_proceso}}`

- Termina un programa usando la señal SIGINT (interrumpir). Esto es normalmente iniciado por el usuario presionando `Ctrl + C`:

`kill -{{2|INT}} {{id_del_proceso}}`

- Señala al sistema operativo para terminar inmediatamente un programa (el cual no tiene oportunidad de capturar la señal):

`kill -{{9|KILL}} {{id_del_proceso}}`

- Señala al sistema operativo para pausar un programa hasta que la señal SIGCONT ("continuar") es recibida:

`kill -{{17|STOP}} {{id_del_proceso}}`

- Envía una señal `SIGUSR1` a todos los procesos con un GID (id de grupo) dado:

`kill -{{SIGUSR1}} -{{id_de_grupo}}`
