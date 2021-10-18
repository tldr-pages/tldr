# cpulimit

> Una herramienta para limitar el uso del CPU de otros procesos.
> Más información: <http://cpulimit.sourceforge.net/>.

- Limita un proceso existente con PID 1234 para que solo use el 25% del CPU:

`cpulimit --pid {{1234}} --limit {{25%}}`

- Limita un programa existente por su nombre de ejecución:

`cpulimit --exe {{programa}} --limit {{25}}`

- Ejecuta un programa determinado y limita su uso a solo el 50% del CPU:

`cpulimit --limit {{50}} -- {{programa arg1 arg2 ...}}`

- Ejecuta un programa, limita el uso del CPU a 50% y corre cpulimit en segundo plano:

`cpulimit --limit {{50}} --background -- {{programa}}`

- Mata su proceso si el uso del CPU del programa supera el 50%:

`cpulimit --limit 50 --kill -- {{programa}}`

- Regula su proceso y sus subprocesos para que ninguno supere el 25% del CPU:

`cpulimit --limit {{25}} --monitor-forks -- {{programa}}`
