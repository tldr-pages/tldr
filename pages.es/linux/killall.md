# killall

> Envía señal de finalización a todas las instancias de un proceso por nombre (debe ser el nombre exacto).
> Todas las señales excepto SIGKILL y SIGSTOP pueden ser interceptadas por el proceso, permitiendo una salida limpia.
> Más información: <https://manned.org/killall>.

- Termina un proceso utilizando la señal SIGTERM (terminar), predeterminada:

`killall {{nombre_del_proceso}}`

- Lista los nombres de señal disponibles (para ser utilizados sin el prefijo 'SIG'):

`killall --list`

- Interactivamente pide confirmación antes de la terminación:

`killall -i {{nombre_del_proceso}}`

- Termina un proceso utilizando la señal SIGINT (interrupción), que es la misma señal enviada pulsando `Ctrl + C`:

`killall -INT {{nombre_del_proceso}}`

- Finaliza -a la fuerza- un proceso:

`killall -KILL {{nombre_del_proceso}}`
