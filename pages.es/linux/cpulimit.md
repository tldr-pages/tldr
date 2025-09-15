# cpulimit

> Una herramienta para limitar el uso del CPU de otros procesos.
> Más información: <https://manned.org/cpulimit>.

- Limita un proceso existente con PID 1234 para que solo use el 25% del CPU:

`cpulimit {{[-p|--pid]}} {{1234}} {{[-l|--limit]}} {{25%}}`

- Limita un programa existente por su nombre de ejecución:

`cpulimit {{[-e|--exe]}} {{programa}} {{[-l|--limit]}} {{25}}`

- Ejecuta un programa determinado y limita su uso a solo el 50% del CPU:

`cpulimit {{[-l|--limit]}} {{50}} -- {{programa argumento1 argumento2 ...}}`

- Ejecuta un programa, limita el uso del CPU a 50% y corre cpulimit en segundo plano:

`cpulimit {{[-l|--limit]}} {{50}} {{[-b|--background]}} -- {{programa}}`

- Elimina su proceso si el uso del CPU del programa supera el 50%:

`cpulimit {{[-l|--limit]}} 50 {{[-k|--kill]}} -- {{programa}}`

- Regula su proceso y sus subprocesos para que ninguno supere el 25% del CPU:

`cpulimit {{[-l|--limit]}} {{25}} {{[-m|--monitor-forks]}} -- {{programa}}`
