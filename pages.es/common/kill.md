# kill

> Envía una señal a un proceso, usualmente relacionado a detener el proceso.
> kill envia una señal para terminar uno o un grupo de procesos.
> Más información: <https://manned.org/kill>.

- Termina un programa usando la señal SIGTERM (terminar) por defecto:

`kill signal PID`

- Lista de las señales disponibles (para ser utilizadas sin el prefijo SIG):

`kill -l`

- Terminar un trabajo en segundo plano:

`kill %{{id_de_tarea}}`

- Termina un programa con  SIGHUP (hang up/colgar). Varios daemons se reiniciaran en lugar de terminar:

`kill -{{1|HUP}} {{process_id}}`

- Terminar un programa mediante SIGINT (interrupt/interrumpir). Esto normalmente lo hace el usuario presionando Ctrl + C:

`kill -{{2|INT}} {{process_id}}`

- Señal del sistema que termina de inmediato un programa (Sin oportunidad de captar la señal):

`kill -{{9|KILL}} {{id_del_proceso}}`

- Señala al sistema operativo para pausar un programa hasta que la señal SIGCONT ("continuar") es recibida:

`kill -{{17|STOP}} {{id_del_proceso}}`

- Envia una señal `SIGUSR1` a todos los procesos con un GID (id de grupo) dado:

`kill -{{SIGUSR1}} -{{id_de_grupo}}`
