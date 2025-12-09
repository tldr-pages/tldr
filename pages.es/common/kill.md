# kill

> Envía una señal a un proceso, usualmente relacionada con detener el proceso.
> Todas las señales a excepción de SIGKILL y SIGSTOP pueden ser interceptadas por el proceso para efectuar una salida limpia.
> Más información: <https://manned.org/kill.1posix>.

- Termina un programa usando la señal SIGTERM (terminar) predeterminada:

`kill {{identificador_del_proceso}}`

- Lista todas las señales disponibles (para utilizarlas sin el prefijo `SIG`):

`kill -l`

- Termina un programa usando la señal SIGHUP (hang up/colgar). Muchos programas residentes (daemons) se recargarán en lugar de terminar:

`kill -{{1|HUP}} {{identificador_del_proceso}}`

- Termina un programa usando la señal SIGINT (interrumpir). Esto es normalmente iniciado por el usuario al presionar `<Ctrl c>`:

`kill -{{2|INT}} {{identificador_del_proceso}}`

- Señala al sistema operativo terminar inmediatamente un programa (el cual no tiene oportunidad de capturar la señal):

`kill -{{9|KILL}} {{identificador_del_proceso}}`

- Señala al sistema operativo pausar un programa hasta que la señal SIGCONT (continuar) sea recibida:

`kill -{{17|STOP}} {{identificador_del_proceso}}`

- Envía una señal `SIGUSR1` a todos los procesos con un GID (id de grupo) dado:

`kill -{{SIGUSR1}} -{{identificador_de_grupo}}`
