# kill

> Envía una señal a un proceso, generalmente relacionada con detener el proceso.
> Todas las señales excepto SIGKILL y SIGSTOP pueden ser interceptadas por el proceso para realizar una salida limpia.
> Más información: <https://manned.org/kill>.

- Termina un programa usando la señal SIGTERM (terminar) predeterminada:

`kill {{id_del_proceso}}`

- Lista valores de señal y sus nombres correspondientes (para ser utilizados sin el prefijo `SIG`):

`kill -L`

- Termina un trabajo en segundo plano:

`kill %{{id_del_trabajo}}`

- Termina un programa usando la señal SIGHUP (hang up). Muchos servicios se recargarán en lugar de terminar:

`kill -{{1|HUP}} {{id_del_proceso}}`

- Termina un programa usando la señal SIGINT (interrupción). Esto es normalmente iniciado por el usuario pulsando `<Ctrl c>`:

`kill -{{2|INT}} {{id_del_proceso}}`

- Indica al sistema operativo terminar inmediatamente un programa (que no tiene oportunidad de capturar la señal):

`kill -{{9|KILL}} {{id_del_proceso}}`

- Indica al sistema operativo detener un programa hasta que se reciba una señal SIGCONT ("continúa"):

`kill -{{17|STOP}} {{id_del_proceso}}`

- Envía una señal `SIGUSR1` a todos los procesos con el GID dado (id del grupo):

`kill -{{SIGUSR1}} -{{id_del_grupo}}`
