# timeout

> Voer een commando uit met een tijdslimiet.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>.

- Voer `sleep 10` uit en beëindig het na 3 seconden:

`timeout 3s sleep 10`

- Stuur een signaal naar het commando nadat de tijdslimiet is verlopen (standaard `TERM`, `kill -l` om alle signalen te tonen):

`timeout {{[-s|--signal]}} {{INT|HUP|KILL|...}} {{5s}} {{sleep 10}}`

- Stuur verbose output naar `stderr` en laat het signaal zien dat is verzonden bij een timeout:

`timeout {{[-v|--verbose]}} {{0.5s|1m|1h|1d|...}} {{commando}}`

- Behoud de exit status van het commando ongeacht of er een timeout is:

`timeout {{[-p|--preserve-status]}} {{1s|1m|1h|1d|...}} {{commando}}`

- Stuur een krachtig `KILL`-signaal na een bepaalde tijd als het commando het initiële signaal negeert bij een timeout:

`timeout {{[-k|--kill-after]}} {{5m}} {{30s}} {{commando}}`
