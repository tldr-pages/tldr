# kill

> Este comando es utilizado para matar/terminar procesos.
> kill envia una señal para terminar uno o un grupo de procesos.
> Mas Informacion: <https://linuxhint.com/linux-kill-command/>.

- Mata un proceso o grupo de procesos.

`kill signal PID`


- Lista de las señales disponibles (para ser utilizadas sin el prefijo SIG):
`kill -l`

- Terminar un trabajo en segundo plano:
`kill %{{job_id}}`

- Termina un programa con  SIGHUP (hang up/colgar). Varios daemons se reiniciaran en lugar de terminar:
`kill -{{1|HUP}} {{process_id}}`

- Terminar un programa mediante SIGINT (interrupt/interrumpir). Esto normalmente lo hace el usuario presionando Ctrl + C:
`kill -{{2|INT}} {{process_id}}`

- Señal de sistema operativo que termina de inmediato un programa (Sin oportunidad de captar la señal):
`kill -{{9|KILL}} {{process_id}}`

- Señal de sistema operativo que pausa un programa hasta que la señal SIGCONT ("continue"/"continuar") se reciva :
`kill -{{17|STOP}} {{process_id}}`

- Envia una señal SIGUSR1 a todos los procesos a los que tengan asignado un GID (group id/id de grupo):
`kill -{{SIGUSR1}} -{{group_id}}`