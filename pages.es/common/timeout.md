# timeout

> Ejecuta un comando con un límite de tiempo.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>.

- Ejecuta `sleep 10` y lo detiene tras 3 segundos:

`timeout 3s sleep 10`

- Envía una señal al comando una vez transcurrido el límite de tiempo (`TERM` por defecto; utiliza `kill -l` para ver la lista completa de señales):

`timeout {{[-s|--signal]}} {{INT|HUP|KILL|...}} {{5s}} {{sleep 10}}`

- Envía una salida detallada a `stderr` que muestre la señal enviada al agotarse el tiempo de espera:

`timeout {{[-v|--verbose]}} {{0.5s|1m|1h|1d|...}} {{comando}}`

- Conserva el estado de salida del comando independientemente de que se agote el tiempo de espera:

`timeout {{[-p|--preserve-status]}} {{1s|1m|1h|1d|...}} {{comando}}`

- Envía una señal `KILL` forzada tras un tiempo determinado si el comando ignora la señal inicial al agotarse el tiempo de espera:

`timeout {{[-k|--kill-after]}} {{5m}} {{30s}} {{comando}}`
