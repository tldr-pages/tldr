# timeout

> Voer een commando uit met een tijdslimiet.
> Meer informatie: <https://www.gnu.org/software/coreutils/timeout>.

- Voer `sleep 10` uit en beëindig het na 3 seconden:

`timeout 3s sleep 10`

- Stuur een signaal naar het commando nadat de tijdslimiet is verlopen (standaard SIGTERM):

`timeout --signal {{INT}} {{5s}} {{sleep 10}}`
